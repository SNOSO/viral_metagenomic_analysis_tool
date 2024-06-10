from collections import defaultdict

def create_kmers(filtered_sequences, kmer_size):
    kmer_counts = defaultdict(int)
    for seq in filtered_sequences:
        for i in range(len(seq) - kmer_size + 1):
            kmer = seq[i:i + kmer_size]
            kmer_counts[kmer] += 1
    return kmer_counts

class BWT:
    def __init__(self, s):
        s = s + '$'
        self.s = s
        self.bwt, self.sa = self.construct_bwt_and_sa(s)
        self.occ = self.construct_occurrences(self.bwt)
        self.c = self.construct_c()

    def construct_bwt_and_sa(self, s):
        rotations = sorted((s[i:] + s[:i], i) for i in range(len(s)))
        bwt = ''.join(rot[-1] for rot, _ in rotations)
        sa = [i for _, i in rotations]
        return bwt, sa

    def construct_occurrences(self, bwt):
        occ = defaultdict(lambda: [0] * len(bwt))
        total_counts = defaultdict(int)
        for i, char in enumerate(bwt):
            total_counts[char] += 1
            for key in total_counts:
                occ[key][i] = total_counts[key]
        return occ

    def construct_c(self):
        sorted_bwt = sorted(self.bwt)
        c = {}
        for i, char in enumerate(sorted_bwt):
            if char not in c:
                c[char] = i
        return c

    def count(self, pattern):
        l, r = 0, len(self.bwt) - 1
        for char in reversed(pattern):
            if char in self.c:
                l = self.c[char] + (self.occ[char][l - 1] if l > 0 else 0)
                r = self.c[char] + self.occ[char][r] - 1
                if l > r:
                    return 0
            else:
                return 0
        return r - l + 1
