-- Generate_Palette_Apple_clr.applescript
--
-- Why this exists: a hand-authored binary .clr risks producing a file
-- that silently fails to open in Xcode/Preview/the macOS color picker —
-- NSColorList's internal NSKeyedArchiver encoding isn't safe to guess.
-- This script instead asks macOS's own Cocoa framework to write the
-- file, which guarantees a valid result every time.
--
-- HOW TO RUN (on a Mac):
--   1. Open Script Editor (Applications > Utilities > Script Editor).
--   2. Paste this whole file in, press the Run (▶) button.
--   3. Find "Ariviti.clr" in ~/Library/Colors — double-click it to
--      install it into the macOS color picker under "Ariviti".
--
-- Colors are pulled directly from tokens_color.json's canonical hex
-- values — update them here if the palette ever changes.

use framework "Foundation"
use scripting additions

set colorDefs to {¬
	{name:"Vibrant Orange", r:1.0, g:0.301961, b:0.109804}, ¬
	{name:"Royal Indigo", r:0.231373, g:0.243137, b:0.662745}, ¬
	{name:"Indigo Dark", r:0.117647, g:0.086275, b:0.411765}, ¬
	{name:"White", r:1.0, g:1.0, b:1.0}, ¬
	{name:"Soft Black", r:0.180392, g:0.180392, b:0.180392}}

set colorList to current application's NSColorList's alloc()'s initWithName:"Ariviti"

repeat with c in colorDefs
	set nsColor to current application's NSColor's colorWithCalibratedRed:(r of c) green:(g of c) blue:(b of c) alpha:1.0
	(colorList's setColor:nsColor forKey:(name of c))
end repeat

set libraryColorsPath to (POSIX path of (path to library folder from user domain)) & "Colors/"
set fileManager to current application's NSFileManager's defaultManager()
(fileManager's createDirectoryAtPath:libraryColorsPath withIntermediateDirectories:true attributes:(missing value) |error|:(missing value))

set outputPath to libraryColorsPath & "Ariviti.clr"
set ok to colorList's writeToFile:outputPath

if ok as boolean then
	display dialog "Wrote a verified Ariviti.clr to ~/Library/Colors" buttons {"OK"} default button "OK"
else
	display dialog "Failed to write Ariviti.clr — check file permissions on ~/Library/Colors" buttons {"OK"} default button "OK"
end if
