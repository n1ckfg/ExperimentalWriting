import os
from aitextgen import aitextgen
from aitextgen.colab import mount_gdrive, copy_file_from_gdrive

os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

model_selection="gpt-neo-125M" # GPT-Neo Pytorch, requires 12GB VRAM
#model_selection="355M" # Stock GPT-2 TF, requires 16GB VRAM
#model_selection="124M" # Stock GPT-2 TF, requires 8GB VRAM
#model_selection="gpt-neo-1.3B" # GPT-Neo Pytorch, requires ??GB VRAM
#model_selection="gpt-neo-2.7B" # GPT-Neo Pytorch, requires ??GB VRAM
#model_selection="gpt-j-6B" # GPT-Neo Pytorch, requires ??GB VRAM

# GPT-Neo Pytorch...
#ai = aitextgen(model="EleutherAI/" + model_selection, to_gpu=True) # gpt-neo-125M, gpt-neo-1.3B, gpt-neo-2.7B, gpt-neo-6B

# Stock GPT-2 TF...
#ai = aitextgen(tf_gpt2=model_selection, to_gpu=True) # 124M, 355M, 774M, 1558M

# Other custom Pytorch...
ai = aitextgen(model="base_models/" + model_selection, to_gpu=True) # gpt2-medium

file_name = "nick_corpus_combo.txt"

ai.train(file_name,
         line_by_line=False,
         from_cache=False,
         num_steps=500,
         generate_every=100,
         save_every=500,
         save_gdrive=False,
         learning_rate=1e-3,
         fp16=False,
         batch_size=1, 
         )

ai = aitextgen(model_folder="trained_model", to_gpu=True)

ai.generate()
