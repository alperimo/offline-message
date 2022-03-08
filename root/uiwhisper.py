import gameInfo

	def SendWhisper(self):
		
		gameInfo.WHISPER_GET = 1
		gameInfo.MESSAGE_GONDERILEN = text

	def Close(self):
		if "#"+str(self.targetName)+"#" in gameInfo.WHISPER_YOLLANANLAR:
			gameInfo.WHISPER_YOLLANANLAR.remove("#"+str(self.targetName)+"#")