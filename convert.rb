require 'json'
require 'date'

data = JSON.parse(File.open('./bookmarks.json').read)

result = data.map do |item|
    {
        :title => item["title"],
        :created => Time.at(item["created"].to_i).to_date.to_s
    }
end.to_json

File.open('./bookmarks.converted.json', 'w').write(result)
