# EmmyLua

## 代码示例

``` Lua

---@class Transport @父类
---@public field name string
local transport = {}

function transport:move()end

---@class Car : Transport @Car继承自Transport
local car = {}
function car:move()end

---@class Ship : Transport @Ship继承自Transport
local ship = {}

---@param type number @参数type说明
---@return Car|Ship @返回类型可能是Car也有可能是Ship
local function create(type)
-- 略
end

local obj = create(1)
---此时obj可代码提示

---@type Car
local obj2
---此时obj2可代码提示

local list = { obj, obj2 }
---@param v Transport
for _, v in ipairs(list) do
---此时v可代码提示
end

-------------------------------------------------------------------------------
-- 字典类型
-------------------------------------------------------------------------------

---@type table<string, Car>
local dict = {}

local car = dict['key']
-- car. 可以出现代码提示

for key, car in pairs(dict) do
    -- car. 可以出现代码提示
end

-------------------------------------------------------------------------------
-- 数组类型
-------------------------------------------------------------------------------
---@type Car[]
local list = {}

local car = list[1]
-- car. 可以出现代码提示

for i, car in ipairs(list) do
    -- car. 可以出现代码提示
end

```