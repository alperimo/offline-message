--[[

TR: Tüm özel sistemler, fonksiyonlar, methodlar, ve yol...
TRL : All Special Systems, funcs, method and the way to...

Geliþtirici : .. Fatihbab34™ ..
Paketler ; LuaToPython, PythonToLua, PythonIslem
Fonksiyonlar ; "split('#blabla#blabla#', '#'), systems.getinput('PythonIslem'), io funcs(open, remove, write, read, readline, readlines), table forms, pc.getqf(), pc.setqf()"

--]]

quest systems begin
	state start begin
		
		when login begin
			cmdchat("PythonToLua "..q.getcurrentquestindex())
			
			-- Çevrim Dýþý Gelen Mesajlarý Kontrol --
			local messages_kontrol = io.open('/usr/game/share/locale/turkey/quest/systems/kapali_mesajlar/'..pc.get_name()..'.cfg', 'r')
			if messages_kontrol then
				--cmdchat("LuaToPython #cevrimdisi_mesaj_geldi_icon_open#")
				for line in messages_kontrol:lines() do
					local satir = string.gsub(line,' ','_')
					cmdchat('LuaToPython #cevrimdisi_gelen_mesaj|'..satir)
				end
				os.remove('/usr/game/share/locale/turkey/quest/systems/kapali_mesajlar/'..pc.get_name()..'.cfg')
			end
		end

		when button begin
			local gelen = systems.getinput("PYTHONISLEM")

			if string.find(gelen, "kapali_mesaj_yolla#") then
				local mes = systems.getinput("MESSAGE_MESAJ_AL")
				local bol = systems.split(gelen, "#")
				local message = string.gsub(mes,' ','_')
				if string.len(message) >= 54 then
					local mes2 = systems.getinput("MESSAGE_MESAJ_AL_2")
					local message2 = string.gsub(mes2,' ','_')
					local name = bol[2]
					local open = io.open('/usr/game/share/locale/turkey/quest/systems/kapali_mesajlar/'..name..'.cfg', 'a+')
					--local zaman = os.date("%c")
					local zaman = os.date("%d/%m/%Y, %H:%m")
					open:write('#'..pc.get_name()..'#'..message..message2..'#'..zaman..'#'..'\\n')
					open:close()
					notice(name..' adlý oyuncuya kapalý mesajýnýz baþarýyla gönderildi.')
				else
					local name = bol[2]
					local open = io.open('/usr/game/share/locale/turkey/quest/systems/kapali_mesajlar/'..name..'.cfg', 'a+')
					--local zaman = os.date("%c")
					local zaman = os.date("%d/%m/%Y, %H:%m")
					open:write('#'..pc.get_name()..'#'..message..'#'..zaman..'#'..'\\n')
					open:close()
					notice(name..' adlý oyuncuya kapalý mesajýnýz baþarýyla gönderildi.')
				end
			end
		end

		function getinput(gelen)
			local input1 = "#quest_input#"
			local input0 = "#quest_inputbitir#"
			cmdchat("LuaToPython "..input1)
			local al = input(cmdchat("PythonIslem "..gelen))
			cmdchat("LuaToPython "..input0)
			return al
		end

		function split(command_, ne)
			return systems.split_(command_,ne)
		end
		
		function split_(string_,delimiter)
			local result = { }
			local from  = 1
			local delim_from, delim_to = string.find( string_, delimiter, from  )
			while delim_from do
				table.insert( result, string.sub( string_, from , delim_from-1 ) )
				from  = delim_to + 1
				delim_from, delim_to = string.find( string_, delimiter, from  )
			end
			table.insert( result, string.sub( string_, from  ) )
			return result
		end

	end
end