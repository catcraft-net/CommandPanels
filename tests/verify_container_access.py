from pathlib import Path

root = Path(__file__).resolve().parents[1]
paths = [
    "src/me/rockyhawk/commandpanels/session/Panel.java",
    "src/me/rockyhawk/commandpanels/session/inventory/InventoryPanelUpdater.java",
    "src/me/rockyhawk/commandpanels/session/inventory/generator/GenerateManager.java",
    "src/me/rockyhawk/commandpanels/session/inventory/listeners/ClickEvents.java",
    "src/me/rockyhawk/commandpanels/session/inventory/listeners/InventoryEvents.java",
]
source = "\n".join((root / path).read_text() for path in paths)
assert ".getHolder()" not in source
assert source.count("getHolder(false)") >= 10
closed_guard = source.index("event.getInventory().getHolder(false)")
current_view = source.index("InventoryView currentView = player.getOpenInventory()", closed_guard)
assert closed_guard < current_view
print("PASS: CommandPanels non-snapshot holder access and close ordering")
