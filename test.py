import sequential, unittest, jieba

class TestSplitMethods(unittest.TestCase):

    def test_refined(self):
        sentence = "It is a test. B ut I am not sure if it is valid."
        result = ["It is a test.", " B ut I am not sure if it is valid."]
        self.assertEqual(sequential.refinedSplit(sentence, "."), result)

    def test_arrray(self):
        array = ["f, s,f ", "ff, sdf"]
        result = ["f,", " s,", "f ", "ff,", " sdf"]
        self.assertEqual(sequential.arraySplit(array, ","), result)

    def test_split(self):
        sentence = "这是一首简单的小情歌，唱着人们心肠的曲折。"
        result = ['这是一首简单的小情歌', '唱着人们心肠的曲折。']
        self.assertEqual(sentence.split("，"), result)

    def test_jieba(self):
        sentence = "这是一首简单的小情歌，唱着人们心肠的曲折。"
        # print(jieba.cut(sentence))
        pieces = jieba.cut(sentence)
        for piece in pieces:
            print(piece)