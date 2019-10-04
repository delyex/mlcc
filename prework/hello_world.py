# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% [markdown]
# #### Copyright 2017 Google LLC.

#%%
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#%% [markdown]
# # 准备工作：Hello World
#%% [markdown]
# **学习目标：**在浏览器中运行 TensorFlow 程序。
#%% [markdown]
# 以下代码块为“Hello World”TensorFlow 程序。
# 
# 其中包含初始化代码（导入 TensorFlow 模块并启用“eager execution”，我们将在后续练习中详细介绍此操作），然后输出“Hello, world!”字符串常量。

#%%
from __future__ import print_function

import tensorflow as tf
try:
  tf.contrib.eager.enable_eager_execution()
except ValueError:
  pass  # enable_eager_execution errors after its first call

tensor = tf.constant('Hello, world!')
tensor_value = tensor.numpy()
print(tensor_value)

#%% [markdown]
# ## 要运行此程序，请执行以下操作
# 
#   1. 点击代码块中的任意位置（例如，点击字词 `import`）。
# 
#   2. 点击代码块左上角的右向三角图标，或按 ⌘/Ctrl+Enter 键。
# 
#      程序需要几秒钟才会运行。如果一切顺利，程序会在代码块正下方显示 `Hello, world!` 字样
# 
# 整个程序仅包含一个代码块。不过，大部分练习都会包含多个代码块，在这种情况下，您应**按从上到下的顺序逐个运行代码块。**
# 
# 不按顺序运行代码块通常会导致错误。
#%% [markdown]
# ## 实用的键盘快捷键
# 
# * **⌘/Ctrl+m,b：**在当前选择的单元格下方创建一个空白代码单元格
# * **⌘/Ctrl+m,i：**中断单元格的运行
# * **⌘/Ctrl+m,h：**显示所有键盘快捷键列表
# * 要查看关于任何 TensorFlow API 方法的文档，请将光标放置在其左括号的正后方，然后按 **Tab** 键：
# 
#   ![TensorFlow tf.constant 方法的弹出式文档](https://download.mlcc.google.cn/mledu-images/tf_pop_up_doc_example.png)

