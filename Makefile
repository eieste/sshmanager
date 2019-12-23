remove_migrations:
	find . -type f -iregex "\.\/[a-z]*\/migrations\/[0-9]+_.*\.py$\" -delete