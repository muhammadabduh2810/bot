# if you can read this, this meant you use code from Ubot | Ram Project
# this code is from somewhere else
# please dont hestitate to steal it
# because Ubot and Ram doesn't care about credit
# at least we are know as well
# who Ubot and Ram is
#
#
# kopas repo dan hapus credit, ga akan jadikan lu seorang developer
# ©2023 Ubot | Ram Team
import os
import sys
from re import sub
import asyncio
from time import time
from pyrogram import Client, filters, enums
from pyrogram.errors import ChatAdminRequired
from pyrogram.types import ChatPermissions, ChatPrivileges, Message
from . import *
from ubotlibs.ubot.helper.basic import eor
from .profile import extract_user, extract_userid
from ubotlibs.ubot.database.accesdb import *

admins_in_chat = {}

unmute_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_polls=True,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)

async def list_admins(client: Client, chat_id: int):
    global admins_in_chat
    if chat_id in admins_in_chat:
        interval = time() - admins_in_chat[chat_id]["last_updated_at"]
        if interval < 3600:
            return admins_in_chat[chat_id]["data"]

    admins_in_chat[chat_id] = {
        "last_updated_at": time(),
        "data": [
            member.user.id
            async for member in client.get_chat_members(
                chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS
            )
        ],
    }
    return admins_in_chat[chat_id]["data"]


async def extract_user_and_reason(message, sender_chat=False):
    args = message.text.strip().split()
    text = message.text
    user = None
    reason = None
    if message.reply_to_message:
        reply = message.reply_to_message
        if not reply.from_user:
            if (
                reply.sender_chat
                and reply.sender_chat != message.chat.id
                and sender_chat
            ):
                id_ = reply.sender_chat.id
            else:
                return None, None
        else:
            id_ = reply.from_user.id

        if len(args) < 2:
            reason = None
        else:
            reason = text.split(None, 1)[1]
        return id_, reason

    if len(args) == 2:
        user = text.split(None, 1)[1]
        return await extract_userid(message, user), None

    if len(args) > 2:
        user, reason = text.split(None, 2)[1:]
        return await extract_userid(message, user), reason

    return user, reason

@Client.on_message(filters.command(["setgpic"], "") & filters.me)
async def set_chat_photo(client: Client, message: Message):
    zuzu = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    can_change_admin = zuzu.can_change_info
    can_change_member = message.chat.permissions.can_change_info
    if not (can_change_admin or can_change_member):
        await message.reply("Kamu tidak punya akses wewenang")
    if message.reply_to_message:
        if message.reply_to_message.photo:
            await client.set_chat_photo(
                message.chat.id, photo=message.reply_to_message.photo.file_id
            )
            return
    else:
        await message.edit("Balas ke photo untuk set!")



@Client.on_message(filters.command(["ban", "dban"], "") & filters.me)
async def member_ban(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    ky = await message.reply("`Processing...`")
    if not user_id:
        return await ky.edit("Tidak dapat menemukan pengguna.")
    if user_id == client.me.id:
        return await ky.edit("Tidak bisa banned diri sendiri.")
    if user_id in DEVS:
        return await ky.edit("Tidak bisa banned Devs!")
    if user_id in (await list_admins(client, message.chat.id)):
        return await ky.edit("Tidak bisa banned admin.")
    try:
        mention = (await client.get_users(user_id)).mention
    except IndexError:
        mention = (
            message.reply_to_message.sender_chat.title
            if message.reply_to_message
            else "Anon"
        )
    if message.command[0][0] == "d":
        await message.reply_to_message.delete()
    msg = f"**Banned User:** {mention}\n**Banned By:** {message.from_user.mention}\n"
    if reason:
        msg += f"**Reason:** {reason}"
    try:
        await message.chat.ban_member(user_id)
        await ky.edit(msg)
    except ChatAdminRequired:
        return await ky.edit("**Anda bukan admin di group ini !**")



@Client.on_message(filters.command(["unban"], "") & filters.me)
async def member_unban(client: Client, message: Message):
    reply = message.reply_to_message
    ini = await message.reply("`Processing...`")
    if reply and reply.sender_chat and reply.sender_chat != message.chat.id:
        return await ini.edit("Tidak bisa unban ch")

    if len(message.command) == 2:
        user = message.text.split(None, 1)[1]
    elif len(message.command) == 1 and reply:
        user = message.reply_to_message.from_user.id
    else:
        return await ini.edit(
            "Berikan username, atau reply pesannya."
        )
    try:
        await asyncio.sleep(0.1)
        await message.chat.unban_member(user)
        
        umention = (await client.get_users(user)).mention
        await ini.edit(f"Unbanned! {umention}")
    except ChatAdminRequired:
        return await ini.edit("**Anda bukan admin di group ini !**")



@Client.on_message(filters.command(["pin", "unpin"], "") & filters.me)
async def pin_message(client: Client, message):
    if not message.reply_to_message:
        return await message.reply("Balas ke pesan untuk pin/unpin .")
    await message.edit("`Processing...`")
    r = message.reply_to_message
    if message.command[0][0] == "u":
        await r.unpin()
        return await message.edit(
            f"**Unpinned [this]({r.link}) message.**",
            disable_web_page_preview=True,
        )
    try:
        await r.pin(disable_notification=True)
        await message.edit(
            f"**Pinned [this]({r.link}) message.**",
            disable_web_page_preview=True,
        )
    except ChatAdminRequired:
        return await message.edit("**Anda bukan admin di group ini !**")


@Client.on_message(filters.command(["mute"], "") & filters.me)
async def mute(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message)
    nay = await message.reply("`Processing...`")
    if not user_id:
        return await nay.edit("Pengguna tidak ditemukan.")
    if user_id == client.me.id:
        return await nay.edit("Tidak bisa mute diri sendiri.")
    if user_id in DEVS:
        return await nay.edit("Tidak bisa mute dev!")
    if user_id in (await list_admins(client, message.chat.id)):
        return await nay.edit("Tidak bisa mute admin.")
    
    mention = (await client.get_users(user_id)).mention
    msg = (
        f"**Muted User:** {mention}\n"
        f"**Muted By:** {message.from_user.mention if message.from_user else 'Anon'}\n"
    )
    if reason:
        msg += f"**Reason:** {reason}"
    try:
        await message.chat.restrict_member(user_id, permissions=ChatPermissions())
        await nay.edit(msg)
    except ChatAdminRequired:
        return await nay.edit("**Anda bukan admin di group ini !**")



@Client.on_message(filters.command(["unmute"], "") & filters.me)
async def unmute(client: Client, message: Message):
    user_id = await extract_user(message)
    nanay = await message.reply("`Processing...`")
    if not user_id:
        return await nanay.edit("Pengguna tidak ditemukan.")
    try:
        await message.chat.restrict_member(user_id, permissions=unmute_permissions)
        
        umention = (await client.get_users(user_id)).mention
        await nanay.edit(f"Unmuted! {umention}")
    except ChatAdminRequired:
        return await nanay.edit("**Anda bukan admin di group ini !**")


@Client.on_message(filters.command(["kick", "dkick"], "") & filters.me)
async def kick_user(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message)
    ny = await message.reply("`Processing...`")
    if not user_id:
        return await ny.edit("Pengguna tidak ditemukan.")
    if user_id == client.me.id:
        return await ny.edit("Tidak bisa kick diri sendiri.")
    if user_id == DEVS:
        return await ny.edit("Tidak bisa kick dev!.")
    if user_id in (await list_admins(client, message.chat.id)):
        return await ny.edit("Tidak bisa kick admin.")
    
    mention = (await client.get_users(user_id)).mention
    msg = f"""
**Kicked User:** {mention}
**Kicked By:** {message.from_user.mention if message.from_user else 'Anon'}"""
    if message.command[0][0] == "d":
        await message.reply_to_message.delete()
    if reason:
        msg += f"\n**Reason:** `{reason}`"
    try:
        await message.chat.ban_member(user_id)
        await ny.edit(msg)
        await asyncio.sleep(1)
        await message.chat.unban_member(user_id)
    except ChatAdminRequired:
        return await ny.edit("**Anda bukan admin di group ini !**")


@Client.on_message(
    filters.group & filters.command(["promote", "fullpromote"], "") & filters.me
)
async def promotte(client: Client, message: Message):
    user_id = await extract_user(message)
    nan = await message.reply("`Processing...`")
    if not user_id:
        return await nan.edit("Pengguna tidak ditemukan.")
    rd = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    try: 
        if message.command[0][0] == "f":
            await message.chat.promote_member(
                user_id,
                privileges=ChatPrivileges(
                    can_manage_chat=True,
                    can_delete_messages=True,
                    can_manage_video_chats=True,
                    can_restrict_members=True,
                    can_change_info=True,
                    can_invite_users=True,
                    can_pin_messages=True,
                    can_promote_members=True,
                ),
            )
            umention = (await client.get_users(user_id)).mention
            return await nan.edit(f"Fully Promoted! {umention}")

        await message.chat.promote_member(
            user_id,
            privileges=ChatPrivileges(
                can_manage_chat=True,
                can_delete_messages=True,
                can_manage_video_chats=True,
                can_restrict_members=True,
                can_change_info=False,
                can_invite_users=True,
                can_pin_messages=True,
                can_promote_members=False,
            ),
        )
        umention = (await client.get_users(user_id)).mention
        await nan.edit(f"Promoted! {umention}")
    except ChatAdminRequired:
        return await nan.edit("**Anda bukan admin di group ini !**")


@Client.on_message(
    filters.group
    & filters.command(["cdemote"], [""])
    & filters.user(DEVS)
    & ~filters.me
)
@Client.on_message(filters.group & filters.command(["demote"], "") & filters.me)
async def demote(client: Client, message: Message):
    user_id = await extract_user(message)
    nn = await message.reply("`Processing...`")
    if not user_id:
        return await nn.edit("Pengguna tidak ditemukan")
    if user_id == client.me.id:
        return await nn.edit("Tidak bisa demote diri sendiri.")
    await message.chat.promote_member(
        user_id,
        privileges=ChatPrivileges(
            can_manage_chat=False,
            can_delete_messages=False,
            can_manage_video_chats=False,
            can_restrict_members=False,
            can_change_info=False,
            can_invite_users=False,
            can_pin_messages=False,
            can_promote_members=False,
        ),
    )
    umention = (await client.get_users(user_id)).mention
    await nn.edit(f"Demoted! {umention}")


add_command_help(
    "admin",
    [
        [f"ban [reply/username/userid]", "Ban pengguna."],
        [f"unban [reply/username/userid]", "Unban pengguna.",],
        [f"kick [reply/username/userid]", "kick pengguna dari group."],
        [f"promote `or` .fullpromote","Promote pengguna.",],
        [f"demote", "Demote pengguna."],
        [f"mute [reply/username/userid]","Mute pengguna.",],
        [f"unmute [reply/username/userid]","Unmute someone.",],
        [f"pin [reply]","to pin any message.",],
        [f"unpin [reply]","To unpin any message.",],
        [f"setgpic [reply ke image]","To set an group profile pic",],
    ],
)
