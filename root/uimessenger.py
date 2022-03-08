
#deðiþtir
class MessengerMemberItem(MessengerItem):

	STATE_OFFLINE = 0
	STATE_ONLINE = 1
	STATE_MOBILE = 2

	IMAGE_FILE_NAME = {	"ONLINE" : "d:/ymir work/ui/game/windows/messenger_list_online.sub",
						"OFFLINE" : "d:/ymir work/ui/game/windows/messenger_list_offline.sub",
						"MOBILE" : "d:/ymir work/ui/game/windows/messenger_list_mobile.sub", }

	def __init__(self, getParentEvent):
		MessengerItem.__init__(self, getParentEvent)
		self.key = None
		self.state = self.STATE_OFFLINE
		self.mobileFlag = False
		self.Offline()

	def GetStepWidth(self):
		return 15

	def SetKey(self, key):
		self.key = key

	def IsSameKey(self, key):
		return self.key == key

	def IsOnline(self):
		if self.STATE_ONLINE == self.state:
			return True

		return False

	def IsMobile(self):
		if self.STATE_MOBILE == self.state:
			return True

		return False

	def Online(self):
		self.image.LoadImage(self.IMAGE_FILE_NAME["ONLINE"])
		self.state = self.STATE_ONLINE

	def Offline(self):
		if self.mobileFlag:
			self.image.LoadImage(self.IMAGE_FILE_NAME["MOBILE"])
			self.state = self.STATE_MOBILE

		else:
			self.image.LoadImage(self.IMAGE_FILE_NAME["OFFLINE"])
			self.state = self.STATE_OFFLINE

	def SetMobile(self, flag):
		self.mobileFlag = flag

		if not self.IsOnline():
			self.Offline()

	def CanWhisper(self):
		#if self.IsOnline():
		#	return True

		return True

	def OnWhisper(self):
		#if self.IsOnline():
		self.getParentEvent().whisperButtonEvent(self.GetName())

	def OnMobileMessage(self):
		if not uiGameOption.MOBILE:
			return

		if not self.IsMobile():
			return

		self.getParentEvent().SendMobileMessage(self.GetName())

	def Select(self):
		MessengerItem.Select(self)
		
		

class MessengerWindow(ui.ScriptWindow): #to-in		
	#deðiþtir
	def OnDoubleClickItem(self, item):

		if not self.selectedItem:
			return

		#if self.selectedItem.IsOnline():
		self.OnPressWhisperButton()

		if self.selectedItem.IsMobile():
			self.OnPressMobileButton()