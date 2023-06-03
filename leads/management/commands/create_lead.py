from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandParser

class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('first_name', type=str)
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        print(f"hello world {options['first_name']}")