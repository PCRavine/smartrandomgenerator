 Smart Random Generator Pro

A powerful, feature-rich web application for creating custom random tables for TTRPGs (Tabletop Role-Playing Games). Generate encounters, loot, NPCs, plot hooks, and more with advanced features like weighted probabilities, roll chains, and combo builders.

https://img.shields.io/badge/Version-2.0-blue.svg
https://img.shields.io/badge/PWA-Ready-green.svg
https://img.shields.io/badge/Offline-Supported-yellow.svg
✨ Features
🎯 Core Functionality

    Custom Random Tables - Create unlimited tables with weighted or unweighted entries

    Dice Roller - Standard RPG dice (d4, d6, d8, d10, d12, d20, d100) plus custom formulas

    Weighted Probabilities - Control rarity with entry weights (1-100)

    Roll Chains - Automatically roll on other tables after specific results

    Multi-Table Rolls - Roll multiple tables simultaneously

    Combo Builder - Combine multiple table results into formatted templates

    Roll History - Track your rolls with pinning and quick reroll options

🎨 User Experience

    Progressive Web App (PWA) - Install on your device and use offline

    Multiple Themes - Light, Dark, and color variants (Purple, Green, Red, Orange)

    Responsive Design - Works perfectly on desktop, tablet, and mobile

    Drag & Drop - Reorder table entries intuitively

    Search & Filter - Find tables by name, tags, or type

    Favorites - Star your most-used tables for quick access

📊 Advanced Features

    Anti-Repetition System - Avoids repeating recent results

    Cryptographically Secure RNG - True random number generation

    Export/Import - Backup your tables or share with others

    Table Packs - Pre-made collections for different genres

    Statistics - Track your most-used tables and roll counts

    Print/PDF - Export tables for offline reference

🚀 Quick Start
Creating Your First Table

    Click "+ New Table" in the header

    Enter a name and description

    Add entries (one per line)

    Enable "Use weighted entries" for rarity control (optional)

    Add tags for organization

    Click "Save Table"

Rolling Tables

    Quick Roll - Click the 🎲 button on any table in the main list

    Table View - Open a table and use Roll, Roll 3x, or Roll with Advantage

    Multi-Table - Select multiple tables and roll them together

    Dice Roller - Access from the tabs for standard dice or custom formulas

Using Roll Chains

    Edit any table

    Click "+ Add Chain" on any entry

    Select which table to roll automatically after that result

    Save and test - chains execute automatically!

Building Combos

    Click "✨ Combo Builder" in the action bar

    Write a template using {0}, {1}, etc. as placeholders

    Assign tables to each placeholder

    Save for quick access or roll immediately

Example Templates:

    {0} appears at {1} carrying {2}

    Help {0} defeat {1} in {2}

    Find {0} and {1} worth {2} gold

📚 Table Packs

The app includes ready-to-use table collections:
🗡️ Fantasy Starter Pack

    Random Encounters, NPC Names, Treasure Hoard, Quest Hooks, Tavern Names, Magic Items, Dungeon Rooms, Weather, Traps, Rumors, Settlements

🐉 D&D 5e Essentials

    Trinkets (PHB), Potion Effects, Spell Scrolls, Wild Magic Surge, Critical Hits, Tavern Events

🌃 Cyberpunk Generator

    Street Names, Corp Missions, Cyberware, District Events, Vehicle Types

💡 Pro Tips
Weighted Tables

    Common: Weight 8-12

    Uncommon: Weight 4-7

    Rare: Weight 2-3

    Very Rare: Weight 1

Dice Formulas in Entries

Use {dice formulas} directly in your entries:

    Deal {2d6+3} damage

    Find {3d6*10} gold coins

    Restores {2d8+2} HP

Organization

    Use tags liberally (combat, loot, npcs, locations, etc.)

    Favorite your most-used tables

    Export regularly to backup your data

    Use table packs as starting points and customize

🔧 Technical Details
Browser Support

    ✅ Chrome/Edge 88+

    ✅ Firefox 78+

    ✅ Safari 14+

    ✅ Mobile browsers

Data Storage

All data is stored locally in your browser using localStorage. Your tables persist between sessions but are specific to the browser and device.
Offline Usage

The app works completely offline once loaded. Perfect for gaming sessions without internet access.
Privacy

    No data is sent to external servers

    All processing happens locally in your browser

    Your tables remain private on your device

🆘 Troubleshooting
Common Issues

"Table not found" when rerolling from history

    The original table was deleted or renamed

    Use the main interface to roll instead

Combo Builder says "missing tables"

    Some assigned tables were deleted

    Edit the combo and reassign the missing tables

Rolls feel repetitive

    The anti-repetition system avoids recent results

    For small tables, this might feel restrictive

    Disable by clearing recent rolls (refresh page)

Lost my tables

    Always export important tables as backup

    Check if you're using a different browser or private mode

Export/Import Strategy

    Regular exports - Download JSON backups

    Table packs - Use as templates for new campaigns

    Share combos - Export combo templates to share with your group

🎮 Use Cases
For Game Masters

    Session Prep - Generate encounters, NPCs, and plot hooks

    Improvisation - Handle unexpected player choices

    World Building - Create consistent random tables for your setting

    Loot Distribution - Weight treasures by rarity

For Players

    Character Creation - Random backstories, traits, and names

    Downtime Activities - Generate creative outcomes

    Quick References - Access game rules and randomizers

For Game Designers

    Playtesting - Rapidly generate test scenarios

    Balance Testing - Use weights to tune probability distributions

    Content Creation - Build comprehensive random tables for publications

📱 PWA Installation
Desktop

    Click the install icon in your browser's address bar

    Or go to File → "Install Smart Random Generator Pro"

Mobile

    Open in Chrome/Safari

    Tap Share → "Add to Home Screen"

    Launch like a native app

🔄 Version History
v2.0 - Current

    Combo Builder with template system

    Roll Chains for automatic follow-up rolls

    History sidebar with pinning

    Table Packs with pre-made content

    Enhanced mobile experience

    Drag & drop reordering

    Anti-repetition system

v1.0 - Initial Release

    Basic table creation and rolling

    Weighted probabilities

    Dice roller

    Theme support

🤝 Contributing

This is a standalone web application. To customize:

    Download the HTML file

    Edit the JavaScript sections

    Add your own table packs in the tablePacks object

    Modify themes in the CSS variables

📄 License

Free for personal and commercial use. Attribution appreciated but not required.
🎲 Happy Gaming!

Whether you're running a epic fantasy campaign, sci-fi adventure, or horror mystery, Smart Random Generator Pro helps you create memorable, dynamic experiences for your players.

Need help? The app includes extensive tooltips and help modals. Most features have explanations accessible through the interface.
