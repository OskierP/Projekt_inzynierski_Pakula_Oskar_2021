class coleCole:

    def __init__(self, list, index, n):
        self.list = list
        self.index = index
        self.n = n

        self.name = str(list[index][0])
        self.epsilon_inf = float(list[index][1])
        self.sigma0 = float(list[index][-1])

        self.epsilon_n = coleCole.epsilon(list, index, n)
        self.tau_n = coleCole.tau(list, index, n)
        self.alpha_n = coleCole.alpha(list, index, n)

    def get_name(self):
        return self.name

    def get_sigma0(self):
        return self.sigma0

    def get_epsilon_inf(self):
        return self.epsilon_inf

    @classmethod
    def epsilon(cls, list, index: int, n: int):
        eps_n = []

        for i in range(n):
            eps_n.append(float(list[index][2 + i * 3]))
            # print(eps_n)
        return eps_n

    def get_epsilon(self):
        return self.epsilon_n

    @classmethod
    def tau(cls, list, index: int, n: int):
        tau_n = []

        for i in range(n):
            tau_n.append(float(list[index][3 + i * 3]) * 10 ** (-12 + 3 * i))
            # print(tau_n)
        return tau_n

    def get_tau(self):
        return self.tau_n

    @classmethod
    def alpha(cls, list, index: int, n: int):
        alpha_n = []

        for i in range(n):
            alpha_n.append(float(list[index][4 + i * 3]))
            # print(alpha_n)
        return alpha_n

    def get_alpha(self):
        return self.alpha_n
