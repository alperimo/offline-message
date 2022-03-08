import gameInfo
import event
import net
import localegame

	def __ServerCommand_Build(self):
		serverCommandList={
			## New System Plugin ##
			"PythonToLua"			: self.__PythonToLua, # .python to Quest
			"PythonIslem"			: self.__PythonIslem, # .python to Quest
			"LuaToPython"			: self.__LuaToPython, # Quest to .python
			## END - New System Plugin - END ##
		}

	def OpenQuestWindow(self, skin, idx):
		if gameInfo.INPUT == 1:
			return
		self.interface.OpenQuestWindow(skin, idx)


	def __PythonToLua(self, id):
		gameInfo.PYTHONTOLUA = int(id)

	def __PythonIslem(self, PythonIslem):
		if PythonIslem == "PYTHONISLEM":
			net.SendQuestInputStringPacket(gameInfo.PYTHONISLEM)
		elif PythonIslem == "MESSAGE_MESAJ_AL":
			net.SendQuestInputStringPacket(str(gameInfo.MESSAGE_MESAJ))
		elif PythonIslem == "MESSAGE_MESAJ_AL_2":
			net.SendQuestInputStringPacket(str(gameInfo.MESSAGE_MESAJ2))
		elif PythonIslem == "MESSAGE_NAME":
			net.SendQuestInputStringPacket(str(gameInfo.MESSAGE_NAME))

	def __LuaToPython(self, LuaToPython):
		if LuaToPython.find("#quest_input#") != -1:
			gameInfo.INPUT = 1
		elif LuaToPython.find("#quest_inputbitir#") != -1:
			gameInfo.INPUT = 0

		elif LuaToPython.find("#cevrimdisi_gelen_mesaj|") != -1:
			bol = LuaToPython.split("#")
			chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, bol[2], str(bol[2]) + " : " + str(bol[3].replace("_", " ")) + " |cFF00FFFF|H|h[" + str(bol[4].replace("_", " ")) + "] ")
			self.interface.RecvWhisper(bol[2])

	def OnRecvWhisperError(self, mode, name, line):
		if locale.WHISPER_ERROR.has_key(mode):
			if mode == 1:
				if gameInfo.WHISPER_GET == 1:

					if str(name).find("[") != -1:
						chat.AppendWhisper(chat.WHISPER_TYPE_SYSTEM, name, "GM'lere kapalý mesaj gönderemezsiniz.")
						return

					message = gameInfo.MESSAGE_GONDERILEN
					if len(message) > 100:
						chat.AppendChat(chat.CHAT_TYPE_INFO, "100'den fazla karakter içeren bir kapalý mesaj gönderemezsin.")
						return

					if not "#"+str(name)+"#" in gameInfo.WHISPER_YOLLANANLAR:
						chat.AppendWhisper(chat.WHISPER_TYPE_SYSTEM, name, localegame.WHISPER_OFFLINE % name)
						gameInfo.WHISPER_YOLLANANLAR.append("#"+str(name)+"#")
					
					gameInfo.PYTHONISLEM = "kapali_mesaj_yolla#"+str(name)+"#"
					if len(message) >= 54:
						gameInfo.MESSAGE_MESAJ = message[:54]
						gameInfo.MESSAGE_MESAJ2 = message[54:]
					else:
						gameInfo.MESSAGE_MESAJ = message
					event.QuestButtonClick(gameInfo.PYTHONTOLUA)

					gameInfo.WHISPER_GET = 0
					return

				if gameInfo.WHISPER_GET == 2:
					return
			else:
				chat.AppendWhisper(chat.WHISPER_TYPE_SYSTEM, name, locale.WHISPER_ERROR[mode](name))
		else:
			chat.AppendWhisper(chat.WHISPER_TYPE_SYSTEM, name, "Whisper Unknown Error(mode=%d, name=%s)" % (mode, name))
		self.interface.RecvWhisper(name)