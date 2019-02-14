states = ('Rainy', 'Sunny')

observations = ('walk', 'shop', 'clean')

start_probability = {'Rainy': 0.6, 'Sunny': 0.4}

transition_probability = {
    'Rainy': {'Rainy': 0.7, 'Sunny': 0.3},
    'Sunny': {'Rainy': 0.4, 'Sunny': 0.6},
}

emission_probability = {
    'Rainy': {'walk': 0.1, 'shop': 0.4, 'clean': 0.5},
    'Sunny': {'walk': 0.6, 'shop': 0.3, 'clean': 0.1},
}


# 打印路径概率表
def print_dptable(V):
    print("    "),
    for i in range(len(V)):
        print("%7d" % i, )

        for y in V[0].keys():
            print("%.5s: " % y, )
        for t in range(len(V)):
            print("%.20f" % V[t][y])


def viterbi(obs, states, start_p, trans_p, emit_p):
    """

    :param obs:观测序列
    :param states:隐状态
    :param start_p:初始概率（隐状态）
    :param trans_p:转移概率（隐状态）
    :param emit_p: 发射概率 （隐状态表现为显状态的概率）
    :return:
    """
    # 路径概率表 V[时间][隐状态] = 概率
    V = [{}]
    # 一个中间变量，代表当前状态是哪个隐状态
    path = {}

    # 初始化初始状态 (t == 0)
    for y in states:  # V[t - 1][y0] 要用到
        V[0][y] = start_p[y] * emit_p[y][obs[0]]
        path[y] = [y]
    # print(V)
    # print(type(V[0]))

    # 对 t > 0 跑一遍维特比算法
    for t in range(1, len(obs)):  # t为观测序列索引，y为天气（隐含状态）索引
        print("t:" + str(t))
        V.append({})
        newpath = {}  # 临时变量

        for y in states:
            # 概率 隐状态 =    前状态是y0的概率 * y0转移到y的概率 * y表现为当前状态的概率,s，state 为上一状态
            (prob, state) = max(
                [(V[t - 1][s] * trans_p[s][y] * emit_p[y][obs[t]], s) for s in states])  # V[t - 1][y0] V[0]在上边已经初始化
            print("prob, state"+str((prob, state)))
            # 记录最大概率
            V[t][y] = prob  # t为数字，y为字符串，字典的key
            # print(V)
            # 记录路径
            print("oldpath:" + str(newpath))
            newpath[y] = path[state] + [y]  # path[state] path 为字典，只有两个key,  state 为上一状态，y为当前状态
            print("path[state]:" + str(path[state]))
            print("[y]:" + str([y]))
            print("newpath:" + str(newpath))

        # 不需要保留旧路径
        path = newpath

    print_dptable(V)
    (prob, state) = max([(V[len(obs) - 1][y], y) for y in states])  # 主要比较出到达最后状态时各路径的最大概率
    return (prob, path[state])


def example():
    return viterbi(observations,
                   states,
                   start_probability,
                   transition_probability,
                   emission_probability)


print(example())
