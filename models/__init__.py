#!/usr/bin/python3
"""
Create temporary file storage
"""

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
