local snippet_table = {}

local snip_dir = "./files/"

local function get_fname(file) 
    return file:match "(.+)%..+$"
end


-- TODO: instead of creating this array, list all the files in
-- snip_dir and get file name using the get_fname function.
--
local files = { "one", "two"}

local arrayLength = #(files)


for i = 1, #(files) do
    local f_name = files[i]
    local snippets = require(snip_dir .. f_name)
    snippet_table[f_name] = snippets[f_name]
end

print(snippet_table['one']['b'])




