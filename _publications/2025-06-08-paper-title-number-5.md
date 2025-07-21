---
title: "A Forget-and-Grow Strategy for Deep Reinforcement Learning Scaling in Continuous Control"
collection: publications
category: conferences
permalink: /publication/2025-fog-rl
excerpt: "Deep reinforcement learning for continuous control has recently achieved impressive progress. However, existing methods often suffer from primacy bias, a tendency to overfit early experiences stored in the replay buffer, which limits an RL agent's sample efficiency and generalizability."
date: 2025-06-08
venue: 'ICML'
paperurl: 'https://arxiv.org/abs/2507.02712'
citation: 'Kang Z, Hu C, Luo Y, et al. A Forget-and-Grow Strategy for Deep Reinforcement Learning Scaling in Continuous Control[C]//Forty-second International Conference on Machine Learning.'
---

Deep reinforcement learning for continuous control has recently achieved impressive progress. However, existing methods often suffer from primacy bias, a tendency to overfit early experiences stored in the replay buffer, which limits an RL agent's sample efficiency and generalizability. In contrast, humans are less susceptible to such bias, partly due to infantile amnesia, where the formation of new neurons disrupts early memory traces, leading to the forgetting of initial experiences. 

Inspired by this dual processes of forgetting and growing in neuroscience, in this paper, we propose Forget and Grow (FoG), a new deep RL algorithm with two mechanisms introduced. First, Experience Replay Decay (ER Decay) "forgetting early experience", which balances memory by gradually reducing the influence of early experiences. Second, Network Expansion, "growing neural capacity", which enhances agents' capability to exploit the patterns of existing data by dynamically adding new parameters during training. 

Empirical results on four major continuous control benchmarks with more than 40 tasks demonstrate the superior performance of FoG against SoTA existing deep RL algorithms, including BRO, SimBa,
