import random


def main():
    print(3)


def refinedSplit(self, delimter):
    result = []
    lastPosition = -1
    for i in range(0, len(self)):
        if self[i] == delimter:
            result.append(self[lastPosition + 1: i + 1])
            lastPosition = i
    if lastPosition != len(self) - 1:
        result.append(self[lastPosition + 1: len(self)])
    return result


def arraySplit(self, delimiter):
    result = []
    for i in range(0, len(self)):
        # result += self[i].split(delimiter)
        result += refinedSplit(self[i], delimiter)
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
if __name__ == '__main__':
    print(refinedSplit("It is . fucke me.", "."))
    print(refinedSplit("页面不存在。你可能点击了失效的链接，或者不小心输入了错误的网址。", "。"))

    # print(multiSplit("This is, not any. I don't understand it. This is a harsh test. But why empty?", [",", "."]))
    print(multiSplit("页面不存在。你可能点击了失效的链接，或者不小心输入了错误的网址。", ["。"]))

    print(''.join(mixParagraphs(["页面不存在。你可能点击了失效的链接，或者不小心输入了错误的网址。",
                                 "在国足主场对阵香港的世预赛赛前通气会上，效力于巴列卡诺的国脚张呈栋在接受采访时表示，主场对阵香港的比赛要全力争胜，此外他再次表达了对国安放自己留洋的感谢。",
                                 "至于深圳潮湿的天气，我觉得香港队可能要更加适应，但不管怎样，面对他们国足应该以我为主，全力争胜。",
                                 "女足国门王飞压哨转会法甲球队里昂，成为欧洲豪门俱乐部一员。完成转会之后，王飞表示里昂女足是世界上最好的女足俱乐部了，她终于实现了自己的梦想。",
                                 "尽管加盟顶级豪门无疑要面对非常激烈的竞争，但当前里昂队主力门将布哈迪因为肩部受伤，铁定将缺席接下来的比赛，这也为王飞提供了竞争主力门将的良机。",
                                 "目前，中甲联赛已经进行24轮，深圳宇恒积20分排在第14位，与处在降级区的北京理工平分，只因胜负关系占优排名在前，保级形势不容乐观。"])))

    print(''.join(mixParagraphs(["崔永元当年自己创办的实话实说成为中国内地最受欢迎的综艺节目，但是由于各大卫视的模仿，崔永元的实话实说收视率渐渐下降。",
                                 "9月1日—5日，因此在此期间，诸如《爸爸去哪儿》《偶像来了》《十二道锋味》《歌手是谁》《真心英雄》《天天向上》《星光大道》等热门娱乐综艺节目，都将暂时停播一周。而原本在9月4日播出的《中国好声音》以及9月5日播出的《快乐大本营》目前则挪档至9月6日晚播出。",
                                 "至于深圳潮湿的天气，我觉得香港队可能要更加适应，但不管怎样，面对他们国足应该以我为主，全力争胜。",
                                 "9月2日晚，有网友爆料称央视著名主持人将从央视辞职，而辞职的原因是因为央视目前给他的薪水，在应付巨额诊疗费用后，已经无法维持体面的生活。",
                                 "尽管加盟顶级豪门无疑要面对非常激烈的竞争，但当前里昂队主力门将布哈迪因为肩部受伤，铁定将缺席接下来的比赛，这也为王飞提供了竞争主力门将的良机。",
                                 "9月2日上午，首批抵达装备装上火车，包括35mm口径双管高射炮、155mm口径自行火炮。在火车装载平板上有一条贯穿的白线，装备通过摄像头对齐，保证装上火车后，左右偏差在厘米级别。"])))

    main()
