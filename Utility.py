class Utility:
    '''
    Class used to read testcases for HWs
    '''
    def read_file(self, input_file):
            f = open(input_file, 'r')
            num = int(f.readline())
            vec = []

            for x in range(0, num):
                vec.append(int(f.readline()))

            f.close()
            return vec
