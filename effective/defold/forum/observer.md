May be this can help :)

observer.lua

``` lua
local Observer = {}

local observers_by_msg = {}

local function get_key(url, message)
	url = type(url) == 'string' and msg.url(url) or url
	local game_obj_id = hash_to_hex(url.path)
	local msg_id = hash_to_hex(type(message) == 'string' and hash(message) or message)
	return hash(game_obj_id .. msg_id)
end

local function find(t, e)
    for i, v in ipairs(t) do
        if v == e then return i end
    end
    return 0
end

function Observer.register(url, message)
	local key = get_key(url, message)
	observers_by_msg[key] = observers_by_msg[key] or {}
	table.insert(observers_by_msg[key], msg.url())
end

function Observer.deregister(url, message)
	local key = get_key(url, message)
	local obs = observers_by_msg[key]
	local ob = msg.url()
	assert(obs, 'message not registered: ' .. message)
	local id = find(obs, ob)
	assert(id > 0, 'message not registered: ' .. message)
	table.remove(obs, id)
	if #obs <= 0 then
		observers_by_msg[key] = nil
	end
end

function Observer.notify(message, data)
	local key = get_key(msg.url(), message)
	local obs = observers_by_msg[key]
	if obs then
		for _, ob in pairs(obs) do
			msg.post(ob, message, data)
		end
	end
end

return Observer

```

hero.script

``` lua
local Observer = require('observer')

local function change_hp(self, new_hp)
	self.hp = new_hp
	Observer.notify('change_hp', {hp = new_hp})
end
```

game.gui_script:

``` lua
local Observer = require('observer')

function init(self)
	observable.register('/hero', 'change_hp')
end

function final(self)
	observable.deregister('/hero', 'change_hp')
end

function on_message(self, message_id, message, sender)
	if message_id == hash('hp_changed') then
		print('new hp', message.hp)
	end
end
```