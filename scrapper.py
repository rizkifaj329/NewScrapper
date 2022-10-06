import requests
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, \
    InviteHashExpiredError, ChannelPrivateError, UserAlreadyParticipantError
from telethon.errors import FloodWaitError
from telethon.errors import MultiError

from telethon.tl.types import ContactStatus,UserStatusOnline,UserStatusOffline,UserStatusRecently,UserStatusLastWeek,UserStatusLastMonth,UserStatusEmpty

from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon import types
from telethon.tl.types import ChannelParticipantCreator, ChannelParticipantAdmin
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon import events
import sys
import csv
import os
import subprocess
import configparser
import traceback
import time

import sys
import csv
import traceback
from datetime import date, datetime, timedelta