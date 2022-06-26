from fman import DirectoryPaneCommand
import os

class CinnamonQuickLook(DirectoryPaneCommand):
	def __call__(self):
		file_under_cursor = self.pane.get_file_under_cursor()
		if file_under_cursor:
			os.system("dbus-send --print-reply --dest={dbusDest} {dbusPath} {dbusDest}.ShowFile string:\"{fileName}\" int32:0 boolean:false" \
				.format(fileName = file_under_cursor, dbusDest="org.nemo.Preview", dbusPath = "/org/nemo/Preview"))