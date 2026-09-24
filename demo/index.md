---
version: 0.22
updated: 2026-09-23
file: dm-vault.html
aliases: [help, aide]
tags: [help]
---

# DM Vault cheatsheet

Everything the DM Vault can do, how to write notes for it, and where to change things in `dm-vault.html`. This note is named `index.md`, so it is the main page of the wiki: click the site name or *Main page* to come back to it. Put it at the root of your campaign folder. Search for "help" also finds it.

> [!tip] Try it here
> The dice examples in this page are real. Click `2d8+1d10+3` or 3d6 to roll them.

## Sample chapter

The folder *Chapter 1 - The Ashen Hollow* is a complete example that uses every feature, and a model for your own chapters. Start with [[00 Overview]]: its *Test checklist* (at the bottom) walks through everything.

How the sample is organised (a good layout for your own campaign):

| Folder | What goes in it |
|---|---|
| `Chapter 1 - ...` | `00 Overview` (summary, scenes, what the players can learn), one note per scene (`01 ...`, `02 ...`), and the chapter's rumours |
| `NPCs` | one note per character (`type: npc`) or shopkeeper (`type: merchant`) |
| `Monsters` | one note per creature (`type: monster`), sorted by type: the SRD 5.2 bestiary plus your own |
| `Rules` | rules and conditions (`type: rule`); the 2024 conditions are in `Rules/Conditions` |
| `Images` | maps, portraits, handouts (placeholders in the sample: replace them with your own, same file names) |
| `templates` | Scene, NPC, Merchant and Monster templates for *New note* |

The numbers in front of the scenes (`00`, `01`...) keep them in order in the folder list.

## Online version

DM Vault can be used from a website: the page offers **Open my campaign folder** (the visitor's own notes, never uploaded) and **Try the example campaign** (this campaign, opened from GitHub).

- **The example is read-only:** everything works (dice, initiative, pins, player screen, player notes), but notes cannot be saved. In the editor, the Save button becomes *Download on GitHub*, and *New note* explains how to get your own copy.
- **Where it comes from:** `DEMO_URL` and `DOWNLOAD_URL` at the top of the script (section 1) say where the example and the download page are.
- **Security:** the page can only load data from itself and from that address (Content-Security-Policy at the top of the file). Web links in notes can only be `http(s)` or `mailto` links.
- **Publishing it:** see the guide *Publishing on GitHub*.

## Getting started

- **Open:** double-click `dm-vault.html`, then *Open my campaign folder* and pick the folder with your `.md` files. Folders starting with a dot (like `.obsidian`) are skipped.
- **Browser:** Chrome or Edge do everything. Firefox and Safari can read, but *Save* downloads the file instead of writing it.
- **Reload:** in the sidebar under Tools. Use it after editing notes in Obsidian or another app.
- **Offline:** the file needs no internet at all. Fonts are built in.
- **Themes:** the light theme (near-white page, black text) is the default, even when the computer is in dark mode. *Dark / light mode* in the sidebar switches to the charcoal and gold theme; the choice is remembered.

## Top bar

| Part | What it does |
|---|---|
| Site name (left) | Back to the main page |
| Weather | Click: next day with new weather. Arrow ▾: details |
| Dice | Click: opens the dice terminal. Shows the last result |
| Initiative | Crossed swords: shows or hides the initiative bar under the top bar |
| Player notes | Scroll icon with `2/5`: player notes given on this page; click for the list |
| Player screen | Monitor icon: open, black out or close the players' screen (see *Player screen*) |
| Search box (right) | Suggestions while you type, Enter for full results |

## Keyboard shortcuts

| Key | Where | Action |
|---|---|---|
| `/` | Anywhere | Jump to the search box |
| `Enter` | Search box | Full search results |
| `Ctrl+S` | Editor | Save the note |
| `Tab` | Editor | Insert two spaces |
| `Esc` | Anywhere | Close the weather details, dice terminal, image viewer or suggestions |
| `Enter` | Initiative bar, Name or Init box | Add the creature |
| `↑` `↓` `Enter` `Tab` | Initiative bar, name suggestions | Move in the list, choose a name |
| `Enter` | Initiative bar, a number in the track | Save the change and re-sort |
| `↑` `↓` | Dice command line | Recall earlier commands |
| `←` `→` | Image viewer | Previous / next image |

## Dice roller

Open it with the dice button in the top bar. Click a die button to roll one die, or type in the command line and press Enter. Type `help` in the box for a quick reminder.

| Type | Result |
|---|---|
| `2d8+1d10+3` | Adds dice and numbers. Minus works too: `2d6-1` |
| `d20+5 adv` | Advantage: two d20, keep the highest |
| `d20+5 dis` | Disadvantage: two d20, keep the lowest |
| `4d6kh3` | Keep the 3 highest (`kl3` = keep the 3 lowest) |
| `3d6!` | Exploding dice: a maximum rolls again and adds |
| `3x d20+4` | The same roll 3 times |
| `d%` | Same as d100 |
| `2d6 # fire` | Label after `#`, shown in the log |
| `clear` | Empties the log |

**In the log:** the total is in gold, a natural 20 in green, a natural 1 in red, and dropped dice are struck through. The log is saved in the browser.

### Call of Cthulhu rolls

| Type | Result |
|---|---|
| `cc 60` | d100 against skill 60 |
| `cc 60 b` / `cc 60 bb` | 1 or 2 bonus dice (keep the lowest tens) |
| `cc 60 p` / `cc 60 pp` | 1 or 2 penalty dice (keep the highest tens) |

Result levels, following 7th edition:

| Roll | Level |
|---|---|
| 01 | Critical |
| ≤ skill ÷ 5 | Extreme success |
| ≤ skill ÷ 2 | Hard success |
| ≤ skill | Regular success |
| Above skill | Failure |
| 100 (or 96–100 if skill under 50) | Fumble |

### Dice in your notes

Dice written in a note become clickable (dotted underline):

- **In normal text:** common sizes only, with an optional `+` or `-` number. Example: "the trap deals 3d6", "d20+2".
- **In backticks:** any full expression, like `2d8+1d10+3`.

Clicking one opens the dice terminal and rolls it.

## Initiative bar (D&D)

Click the **crossed swords** in the top bar to show the initiative bar just under it. Click again to hide it: the fight is kept, even if you close the page.

From left to right, the bar shows:

- **R1, R2...:** the round.
- **‹ and Next ›:** pass the turn back or forward. After the last creature, the round goes up.
- **The track:** everyone in turn order, highest first. Each creature shows its name, its initiative and a small tag icon (add a condition). A creature without a number yet shows an empty box with a faint dotted line. The current turn is outlined and stays on the left, with who comes next to its right. Players have a blue edge, monsters a red one.
- **The Add form:** Name, initiative, the Monster / Player switch, and Add (or Enter).
- **End:** ends the fight.

**Adding someone:** type the name and the initiative, then Enter.

| Initiative box | Players | Monsters |
|---|---|---|
| `17` | Yes, their total | Yes, a fixed total |
| `+2` or `-1` | No | Rolls d20+2 or d20-1 |
| `15.5` | Yes: beats a 15 in a tie | Yes |
| empty | Yes: no number yet, placed last | Yes |

- **Name suggestions:** start typing a name and the matching monster notes appear under the box, with their CR, HP and initiative bonus (`gob` → Goblin Boss, Goblin Minion, Goblin Warrior...). If the name is already typed in full, Enter adds it directly. Click one, or use `↑` `↓` and `Enter` (or `Tab`); the cursor then jumps to the initiative box. `Esc` closes the list. In *Player* mode, the suggestions are the players you added before. Groups work too: type `gob x3` and pick Goblin Warrior.
- **Monster / Player:** click the switch to change it. It stays on your last choice.
- **Several at once:** `Goblin x3` adds Goblin 1, 2 and 3. With `+2`, each one rolls its own initiative; with a total, they all share it.
- **Numbering continues:** adding goblins after Goblin 3 gives Goblin 4, and adding a name that is already there numbers it.

**Changing a number:** click any number in the track, type the new one, then Enter or click elsewhere. The track re-sorts right away. For a monster, typing `+2` there rerolls it.

**Conditions:** click the tag icon of a creature to open the condition picker.

- **Pick a condition:** one button per D&D 5e condition (Blinded, Charmed, ..., Unconscious), plus Concentrating. Point at a button to read a short reminder of its effects.
- **Other:** type anything else (Bless, Hex, Hunter's Mark...) and press Enter or Add.
- **Rounds (optional):** fill it before choosing. The condition loses one round at the end of that creature's turn and disappears at 0. The rounds left show next to its name. Going back with ‹ does not give rounds back.
- Conditions stack under the creature's name. Point at one to read its reminder, click it to remove it.
- Adding a condition that is already there replaces it (handy to reset its rounds).

**Removing someone:** click their name. Pointing at a name shows it struck through in red, like a condition. If it was their turn, the turn passes to the next one. An *Undo* button appears under the bar for a few seconds and puts them back exactly where they were.

**End:** monsters leave, players stay with an empty initiative and no conditions for the next fight, back to round 1, and the bar hides.

Ties keep the order in which they were added.

## Weather

- **Click the weather** in the top bar: next day, new weather.
- **Click the arrow ▾:** effect at the table, *Reroll today*, climate, season, and the previous 6 days.
- **Memory:** tomorrow usually looks like today (overcast can turn to light rain, clear rarely jumps to a storm). Temperature drifts toward the season average.
- **Rain and snow:** rain becomes sleet or snow when cold enough. A storm becomes a blizzard in the cold, a sandstorm in the desert.
- **Climates:** Temperate, Northern (cold), Desert, Tropical. **Seasons:** Spring, Summer, Autumn, Winter.
- Changing the climate or season starts fresh and forgets the previous days.
- Saved in the browser.

## Writing notes

### Title and properties

**Picture:** any note with an `image:` property (an NPC, a location...) shows that picture at the top of its infobox; monsters show it at the top of their stat block. Without `image:`, a picture named like the note is used when there is one (`Bessa Thornquill` → `bessa-thornquill.jpg`).

The first `# Heading` of a note becomes the page title. Without one, the file name is used.

Properties at the very top (front matter) become the **infobox** on the right:

```yaml
---
level: 3
location: Thornwood
status: in progress
tags: [goblins, chapter-1]
aliases: [Goblin Den]
---
```

- `tags` and `aliases` are not shown in the infobox. Aliases are other names a link can use.
- Values stay simple: `key: value`, `[a, b]` lists, or `- item` lists on the next lines. Nested values are not supported.

### Links

| Write | Result |
|---|---|
| `[[Goblin]]` | Link to the note named Goblin |
| `[[Goblin\|the sentry]]` | Same link, showing other text |
| `[[Goblin#Actions]]` | Link to a heading in that note |
| `[[#Treasure]]` | Link to a heading in this note |
| `[text](https://...)` | Web link, opens in a new tab |

- A link to a note that does not exist yet is shown in red with a dotted underline.
- Each note lists the notes that link to it under *What links here*.
- In a table, write the `|` of a link as `\|`.

### Embeds and images

| Write | Result |
|---|---|
| `![[Goblin]]` | Shows the whole Goblin note inside this one |
| `![[Goblin#Actions]]` | Shows only that section |
| `![[map.png]]` | Image (`![[map.png\|400]]` sets the width) |
| `![alt](maps/cave.png)` | Image by path |

Images anywhere in the campaign folder are found, first next to the note, then by file name. Click an image to open it full screen: click again for real size, arrows for the next image.

### Formatting

| Write | Result |
|---|---|
| `**bold**` | **bold** |
| `*italic*` | *italic* |
| `~~struck~~` | ~~struck~~ |
| `==highlight==` | ==highlight== |
| `` `code` `` | `code` |
| `---` | Section break (❦) |
| `- [ ] task` | Task list checkbox |

**Comments:** text between double percent signs is never shown, not even in the page. The syntax has to stay inside a code block here, otherwise this page would hide it too:

```markdown
%% Note to self: the sentry is secretly the chief's son %%
```

Tags can also be written inline as a hash sign followed by a word, like `#goblins`. They appear at the bottom of the note and in *All tags*.

The first letter of a note's first paragraph gets a large drop cap.

### Callouts

Write a quote that starts with a type in brackets:

```markdown
> [!warning] Trap
> A tripwire rings bells in the hall.
```

> [!warning] Trap
> A tripwire rings bells in the hall.

- Add `-` after the type to make it folded (click to open): `> [!secret]- DM only`.
- Add `+` to make it foldable but open.

> [!example]- Folded example
> Hidden until clicked.

| Color | Types |
|---|---|
| Slate | note, info, todo |
| Verdigris | abstract, summary, tldr, tip, hint, important |
| Moss | success, check, done |
| Tarnished gold | question, help, faq |
| Rust | warning, caution, attention |
| Oxblood | failure, fail, missing, danger, error, bug |
| Nightshade | example |
| Ash | quote, cite |
| Royal blue | player (see *Player notes* below) |

Any other type (like `secret`) uses the slate color.

## Bestiary (SRD 5.2, 2024 rules)

The `Monsters` folder holds the **341 monsters of the SRD 5.2** (the free rules of the 2024 books, "5.5e"), one note each, sorted by creature type:

| Folder | Monsters | Folder | Monsters |
|---|---|---|---|
| Aberrations | 9 | Giants | 10 |
| Beasts | 83 | Humanoids | 26 |
| Celestials | 13 | Monstrosities | 47 |
| Constructs | 10 | Oozes | 4 |
| Dragons | 45 | Plants | 6 |
| Elementals | 17 | Swarms | 7 |
| Fey | 15 | Undead | 20 |
| Fiends | 29 | | |

- **2024 names:** some monsters changed name in 2024. The goblin is now *Goblin Minion*, *Goblin Warrior* or *Goblin Boss* (and a Fey); many humanoids are *Warrior Infantry*, *Tough*, *Bandit*...
- **Find one:** the search box, the folders in the sidebar, or type its name in the initiative bar (`gob` → every goblin and hobgoblin).
- **Conditions:** the 15 conditions of the 2024 rules are in `Rules/Conditions`. In the stat blocks, the first mention of a condition links to its note and opens in the pin panel. The reminders of the initiative condition picker follow the 2024 rules too.
- **Spellcasters:** spells are listed like in the 2024 books (*At Will*, *1/Day Each*...), with "(level 5 version)" when a spell is cast at a higher level.
- **Initiative:** the data does not include the Initiative of each monster, so it is calculated from its Dexterity. Most monsters are right; powerful ones often add their proficiency bonus in the book (for example a lich or a dragon). Fix it in the `init:` property of the note if you want the exact value.
- **Pictures:** no picture is included. Drop an image named after the monster anywhere in your campaign folder and it appears by itself: `Goblin Warrior` → `goblin-warrior.jpg` (or `.png`, `.webp`). Or fill its `image:` property with any file name.
- **Your own monsters:** add notes anywhere (for example `Monsters/Homebrew`), with the Monster template.
- **Accuracy:** the monsters come from a community transcription of the SRD. It is thorough, but if you spot a difference with the book, correct the note: it is a plain text file.
- **Licence:** the SRD is free to use and share under Creative Commons (CC BY 4.0) as long as the credit stays: see [[About the SRD]], and the source line at the bottom of each monster.

## Monsters (stat blocks)

A note with `type: monster` in its properties is shown as a stat block laid out like the 2024 books. The numbers go in the properties, the traits and actions in the text:

```markdown
---
type: monster
size: Small
creature: Fey
alignment: Chaotic Neutral
ac: 15
init: +2
hp: 10 (3d6)
speed: 30 ft.
str: 8
dex: 15
con: 10
int: 10
wis: 8
cha: 8
saves:
skills: Stealth +6
vulnerabilities:
resistances:
immunities:
condition_immunities:
gear: Leather Armor, Scimitar, Shield, Shortbow
senses: Darkvision 60 ft.; Passive Perception 9
languages: Common, Goblin
cr: 1/4
xp: 50
xp_lair:
image:
---
# Goblin Warrior

## Actions
**Scimitar.** *Melee Attack Roll:* +4, reach 5 ft. *Hit:* 5 (1d6 + 2) Slashing damage.

## Bonus Actions
**Nimble Escape.** The goblin takes the Disengage or Hide action.
```

- **The layout:** AC and Initiative, HP, Speed; the six abilities in two tables with their **MOD** and **SAVE** (a proficient save, listed in `saves:`, is in bold); then Skills, Vulnerabilities, Resistances, Immunities (damage; conditions), Gear, Senses, Languages and CR (XP, or XP in lair; PB).
- **Calculated for you:** modifiers, saves that are not proficient, PB from the CR, and the Initiative from DEX when `init:` is empty.
- **Clickable rolls:** every MOD and SAVE, the Initiative, the skills, `Attack Roll: +4` (and the old `+4 to hit`), damage like `1d6 + 2`, `(Recharge 5–6)` and the HP formula.
- **Empty properties** are simply not shown.
- **Sections:** Traits, Actions, Bonus Actions, Reactions, Legendary Actions are normal `##` headings: add any you need (Lair Actions...).
- **Image:** `image:` is the file name of a picture anywhere in the campaign folder. Without it, an image named like the note is used (`goblin-warrior.jpg`). It is shown at the top of the stat block.
- **Template:** `templates/Monster.md`, then *New note* → Template: Monster.

## Pin panel

A column on the right that stays in place while the story scrolls.

- **Links pin by themselves:** clicking a link to a note whose `type:` is monster, npc, merchant, rule, item, spell, location or handout opens it in the panel, and the page you are reading stays. Ctrl+click (or Shift+click) opens it as a page instead.
- **Any note:** the *Pin* button at the right of the *Note / Edit / Source* tabs.
- **Tabs:** each pinned note is a tab. Click a tab to show it, `×` to unpin it. The panel disappears when nothing is pinned.
- **Resize:** drag the left edge of the panel.
- **Open as page:** at the top right of a pinned note.
- Pins are remembered by the browser.

**Rules notes:** a note with `type: rule` (for example `Rules/Conditions/Frightened.md`) opens in the panel from any link, like `[[Frightened|frightened]]` in a stat block.

### Monsters in combat

- **Adding a monster** to the initiative bar with the same name as its note (`Adult Red Dragon`, or `Goblin Warrior x3`) links it to the note: each copy gets the note's hit points.
- **Empty initiative box:** for a monster with a note, it rolls d20 + its Initiative (`init:`, or its DEX modifier).
- **Auto-pin:** when a monster's turn comes, its stat block is pinned and shown.
- **Hit points:** a pinned monster in combat shows an *In combat* box with every copy and its HP. Click an HP box and type `-12` (damage), `+5` (healing) or a number, then Enter. At 0 HP the name is struck through and the creature is dimmed in the initiative bar.

## Player notes

Mark what the players should receive during a chapter (a clue, a rumour, a letter...) with a **player callout**:

```markdown
> [!player] The letter in the desk
> "Meet me at the old mill at midnight. - R."
```

> [!player] Example: the sentry's whistle
> A bone whistle hangs from the sentry's neck. Three short blasts.

- **Mark as given:** click the title of a player callout. Pointing at it highlights it; once given, the title is struck through and the callout dimmed. Click again to undo. On a folded callout, the title marks it; the rest of the title line still opens it.
- **The list:** the scroll icon in the top bar, next to the initiative swords, shows how many of this page's player notes were given, like `2/5` (grey when the page has none). Click it for the list:
  - click a line to mark it given or not (pointing at it previews the change)
  - click the arrow `↓` at its end to jump to that callout (a folded one opens)
  - *Mark all as not given* resets the page
- **No title:** a player callout without a title is listed by the start of its text.
- **Embeds:** player notes inside an embedded note (`![[Rumours]]`) are listed too, and share their state with that note.
- Given notes are kept by the browser and follow the callout's title: renaming a title makes it not given again.

## Player screen

A second window for the monitor that faces the players. Everything is controlled from your laptop, offline.

**Starting it:** click the **monitor icon** in the top bar, then *Open*. A black window opens: drag it to the players' monitor, then click inside it once to make it full screen (the browser needs that click). The monitor icon is highlighted while the screen is open.

**Showing something:**

- **An image:** point at any image in a note or in the pin panel. A *Show to players* button appears at its top right; click it. The image viewer (click an image) has the same button.
- **A player note:** point at a `[!player]` callout, then *Show to players*: its title and text appear large on the screen. (Showing it does not mark it as given; click its title for that.)
- **In combat:** when a monster's turn comes and its note has an `image:`, the image appears by itself. Turn this off in the monitor menu: *Monster images on their turn*.

**The monitor menu:** *Open* (or *Bring to front*), *Black screen* (hide everything), *Close*, the *Monster images on their turn* switch, and what is shown right now.

- Nothing is shown on the players' screen unless you choose it, apart from monster images in combat when the switch is on. Monster names are never shown.
- **Pop-ups:** if the browser blocks the window, allow pop-ups for the page (icon at the right of the address bar) and click *Open* again.
- **Reloading the page** (F5) disconnects the screen: the next time you show something, the old window closes and a new one opens. Drag it back to the players' monitor.

## Special notes and folders

- **Home page:** a note named `Main Page`, `Home` or `index` replaces the default home page (that is why this cheatsheet, `index.md`, is the main page). If several exist, `Main Page` wins, then `Home`, then `index`. To get the default home page back (folders and tags), rename this note, for example to `Cheatsheet.md`.
- **Templates:** notes in a folder named `templates` are offered in *New note*. In them, `{{title}}`, `{{date}}`, `{{date:DD/MM/YYYY}}` and `{{time}}` are filled in.
- **New note:** sidebar, *New note*, or *New note here* on a folder page.

## Customizing dm-vault.html

Open the file in a text editor and use Ctrl+F on the names below. Keep a backup copy first, and reload the page with Ctrl+F5 after a change.

| To change | Look for |
|---|---|
| Colors (light theme) | `:root` at the top of the CSS |
| Colors (dark theme) | `[data-theme='dark']` |
| Fonts | `--display`, `--serif`, `--mono` in `:root` |
| Accent color (black in light, gold in dark) | `--rubric` |
| Site name | `SITE_NAME` (section 1) |
| Tagline under the name | the `<small>` text in the header |
| Callout types and colors | the `CO` table (section 5) and `.co-` rules in the CSS |
| Properties hidden from the infobox | the list inside `renderBody()` |
| Weather climates and odds | `CLIMATES` (section 9B) |
| Weather names and effects | `wxInfo()` (section 9B) |
| Dice buttons | `DICE_PAD` (section 9C) |
| Initiative bar | section 9D; turn order in `initOrder()`, look in the `.init-tog` and `.ib-` CSS rules |
| Condition list and reminders | `CONDITIONS` (section 9D) |
| Player notes | section 9E; color: `.co-player`, look: `.pl-` rules in the CSS |
| Stat block layout | `statBlockHtml()` (section 9F), look: `.sb` rules in the CSS |
| Types that open in the pin panel | `PIN_TYPES` (section 9F) |
| Look of the players' screen | `psPage()` (section 9G) |
| Drop cap | the `DROP CAP` rule in the CSS (delete it to remove) |
| Search ranking | the `sc +=` lines in `search()` (section 8) |

> [!info] Saved in the browser, not in the vault
> The weather, the dice log, the initiative bar, the given player notes, the pins, the player screen settings and the theme are kept by the browser. Opening the file in another browser or computer starts them fresh.

## Not supported yet

Footnotes, underlined (setext) headings, Mermaid diagrams (shown as code), Dataview queries, block references.

## Coming next

- [x] Initiative bar (D&D)
- [x] Monster stat blocks and pin panel, auto-pin on the monster's turn
- [x] Player screen (images and player notes on a second screen)
- [x] SRD 5.2 bestiary (341 monsters, 15 conditions, 2024 rules)
- [ ] SRD 5.2 spells, magic items and feats, and *Show to players* from the pin panel
- [x] Player notes (mark as given)
- [ ] Chapter checkboxes (mark a chapter done)
- [ ] Loot table generator
- [ ] NPC and merchant generator

## Changelog

| Version | Change |
|---|---|
| 0.22 | Online: *Try the example campaign* (read-only, loaded from GitHub Pages), Save → GitHub download, security policy, safer links |
| 0.21 | 2024 rules: SRD 5.2 bestiary (341 monsters) and conditions, 2024 stat block layout (Initiative, MOD/SAVE, Bonus Actions, Gear), 2024 condition reminders, sample chapter uses the Goblin Warrior |
| 0.20 | Bestiary: the 334 SRD monsters sorted by type, the 15 SRD conditions as rule notes, pictures found by name |
| 0.19 | Initiative: name suggestions from your monster notes (and known players) while typing |
| 0.18 | Sample chapter (The Ashen Hollow) with NPC, merchant, goblin, templates and placeholder images; `image:` shown in any infobox |
| 0.17 | The cheatsheet is now `index.md`, the main page |
| 0.16 | Light theme (black text) is always the default; dark only when chosen |
| 0.15 | Player screen: second window for the players' monitor, Show to players on images and player notes, monster images on their turn |
| 0.14 | Monster stat blocks (`type: monster`), pin panel, rule notes, monsters linked to the initiative (HP, auto-roll, auto-pin) |
| 0.13 | Player notes: no checkboxes (click the title or the list line to mark as given); icon moved to the top bar |
| 0.12 | Player notes: `[!player]` callout (replaces `terminal`), Given checkboxes, list icon next to the tabs. Drop cap no longer pushes the next block sideways |
| 0.11 | Initiative: tag icon instead of + for conditions; no placeholder dash when there is no number |
| 0.10 | Initiative: click a name to remove it (with Undo); the × buttons are gone |
| 0.9 | Initiative: name before number; conditions with reminders and optional rounds, stacked under the name |
| 0.8 | Initiative redesigned: swords button only, full track in a bar under the top bar, +bonus for monsters only, End button |
| 0.7 | Initiative tracker in the top bar: players and monsters, rolled or fixed initiative, rounds, numbered copies |
| 0.6 | Top bar: tools on the left next to the site name, search box on the right |
| 0.5 | Light theme: near-white page and banner, neutral greys, black text and accents |
| 0.4 | Dice roller: terminal box, die buttons, full roll syntax, Call of Cthulhu rolls, clickable dice in notes |
| 0.3 | Weather in the top bar: climates, seasons, effects, previous days |
| 0.2 | New look: charcoal and ash themes, tarnished gold accents, built-in fonts, drop cap |
| 0.1 | Trimmed from the notes wiki: MAC tools removed, renamed DM Vault |
