#!/usr/bin/env python
import os
import sys

def main():
    """Punto di ingresso principale per l'applicazione Django."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Non riesco a importare Django. È installato e disponibile nel tuo ambiente virtuale?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()

