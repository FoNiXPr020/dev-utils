"""CLI runner with dry-run support."""

def run(args):
    if args.get("dry_run"):
        print("[DRY RUN] Would execute:", args)
        return
    print("Executing:", args)

# iteration 4
