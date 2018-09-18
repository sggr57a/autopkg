<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>Description</key>
	<string>Downloads the latest version of Adobe Reader DC and makes a pkg of it then uploads it to the JSS.</string>
	<key>Identifier</key>
	<string>com.github.sggr57a.jss.adobereaderdc</string>
	<key>Input</key>
	<dict>
		<key>CATEGORY</key>
		<string>Testing</string>
	</dict>
	<key>MinimumVersion</key>
	<string>0.4.0</string>
	<key>ParentRecipe</key>
	<string>com.github.autopkg.pkg.AdobeReaderDC</string>
	<key>Process</key>
	<array>
		<dict>
			<key>Arguments</key>
			<dict>
				<key>category</key>
				<string>%CATEGORY%</string>
				<key>prod_name</key>
                                <string>%NAME%</string>
				<key>version</key>
				<string>%version%</string>
			</dict>
			<key>Processor</key>
			<string>JSSImporter</string>
		</dict>
	</array>
</dict>
</plist>
