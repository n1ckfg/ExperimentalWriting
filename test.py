import sys
from aitextgen import aitextgen
from aitextgen.colab import mount_gdrive, copy_file_from_gdrive

argv = sys.argv
argv = argv[argv.index("--") + 1:] # get all args after "--"

ai = aitextgen(model_folder="trained_model", to_gpu=True)

#@title Text Generation Parameters
prompt = argv[0] #"BOB: We hid the substance in the luggage rack, where they'll never find it." #@param {type:"string"}
temperature = float(argv[1]) #1.35 #@param {type:"slider", min:0, max:1.5, step:0.05}
top_p = float(argv[2]) #0.97 #@param {type:"slider", min:0.8, max:0.99, step:0.01}
repetition_penalty = float(argv[3]) #1.1 #@param {type:"slider", min:1, max:1.5, step:0.1}
batch_size = int(argv[4]) #3 #@param {type:"slider", min:1, max:3, step:1}
max_length = int(argv[5]) #512 #@param {type:"slider", min:256, max:2048, step:256}

ai.generate(n=batch_size,
            batch_size=batch_size,
            prompt=prompt,
            max_length=max_length,
            temperature=temperature, 
            top_p=top_p)