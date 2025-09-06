"""
WOLF.py - مكتبة Python غير رسمية للاتصال بمنصة WOLF (Palringo)
نسخة Python من wolf.js

هذه المكتبة تتيح إنشاء البوتات والتطبيقات التي تتصل بمنصة WOLF.
"""

from .src.client.wolf_client import WOLFClient
from .src.commands.command import Command
from .src.commands.command_handler import CommandHandler
from .src.models.message import Message
from .src.config.config_manager import ConfigManager

__version__ = "1.0.0"
__author__ = "Wolf.py Community"
__all__ = ["WOLFClient", "Command", "CommandHandler", "Message", "ConfigManager"]