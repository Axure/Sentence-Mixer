import random


def main():
    print(3)


sentence = "这是一首简单的小情歌，唱着人们心肠的曲折。"
print(sentence.split("，"))


def arraySplit(self, delimiter):
    result = []
    for i in range(0, len(self)):
        result += self[i].split(delimiter)
    return result


def multiSplit(self, delimiters):
    result = [self]
    for x in delimiters:
        result = arraySplit(result, x)
    return result


# from the internet:
def weighted_choice_sub(weights):
    rnd = random.random() * sum(weights)
    for i, w in enumerate(weights):
        rnd -= w
        if rnd < 0:
            return i


# We need to let the neighbors less likely to be in the same paragraph.
# It is more of a math problem I think.
# How to measure the randomness?
def mixParagraphs(self):
    sentencePool = []
    sentenceLength = []

    for x in self:
        this = multiSplit(x, ["，", "。", "！", "？"])
        sentencePool.append(this)
        sentenceLength.append(len(this))

    totalLength = sum(sentenceLength)
    result = []

    while totalLength > 0:
        indexToAdd = weighted_choice_sub(sentenceLength)
        # Decrease the length, make the data consistent.
        sentenceLength[indexToAdd] -= 1
        totalLength -= 1

        result.append(sentencePool[indexToAdd][0])
        sentencePool[indexToAdd].pop(0)

    return result


# ["1,", "2"].arraySplit(",")
# print(arraySplit(["fdssd, fdsfds,f ", "fdsfsdf, fdsfsdf"], ","))

# print(multiSplit("This is, not any. I don't understand it. This is a harsh test. But why empty?", [",", "."]))
print(multiSplit("页面不存在。你可能点击了失效的链接，或者不小心输入了错误的网址。", ["。"]))

print(mixParagraphs(["页面不存在。你可能点击了失效的链接，或者不小心输入了错误的网址。",
                     "在国足主场对阵香港的世预赛赛前通气会上，效力于巴列卡诺的国脚张呈栋在接受采访时表示，主场对阵香港的比赛要全力争胜，此外他再次表达了对国安放自己留洋的感谢。",
                     "至于深圳潮湿的天气，我觉得香港队可能要更加适应，但不管怎样，面对他们国足应该以我为主，全力争胜。",
                     "女足国门王飞压哨转会法甲球队里昂，成为欧洲豪门俱乐部一员。完成转会之后，王飞表示里昂女足是世界上最好的女足俱乐部了，她终于实现了自己的梦想。",
                     "尽管加盟顶级豪门无疑要面对非常激烈的竞争，但当前里昂队主力门将布哈迪因为肩部受伤，铁定将缺席接下来的比赛，这也为王飞提供了竞争主力门将的良机。",
                     "目前，中甲联赛已经进行24轮，深圳宇恒积20分排在第14位，与处在降级区的北京理工平分，只因胜负关系占优排名在前，保级形势不容乐观。"]))

main()
