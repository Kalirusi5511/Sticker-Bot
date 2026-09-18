# ... (Imports, DB-Funktionen, Bot-Setup wie vorher)

# --- Berechtigungs-Helfer ---
def is_owner_or_admin(interaction: discord.Interaction) -> bool:
    if interaction.guild.owner_id == interaction.user.id:
        return True
    if interaction.user.guild_permissions.administrator:
        return True
    return False

# --- /sticker add ---
@sticker_group.command(name="add", ...)
async def sticker_add(...):
    # ... (wie vorher)

# --- /sticker list ---
@sticker_group.command(name="list", ...)
async def sticker_list(...):
    # ... (wie vorher)

# --- /sticker show ---
@sticker_group.command(name="show", ...)
async def sticker_show(...):
    # ... (wie vorher)

# --- /sticker delete (NEU mit Owner/Admin-Check) ---
@sticker_group.command(name="delete", ...)
async def sticker_delete(...):
    # ... (siehe oben)
