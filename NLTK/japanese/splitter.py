import japanese_splitter
import writter

text = '私は子供です。だから、お菓子を食べてが好き！'
text = 'アメリカの調査会社によると、去年工場で生産して店などに出したスマートフォンは世界で１４億台でした。おととしに比べて４％ぐらい少なくなりました。２年続けて少なくなって、世界でいちばんたくさん売っている中国では１０％ぐらい少なくなりました。'

x = japanese_splitter.jTokenize(text)
writter.hey(x,'output.txt','w',False)






