import torch
import torch.nn as nn 
import argparse
import sys
sys.path.append("../../")

from general.mutils import load_args
from experiments.graph_coloring.train import TrainGraphColoring, args_to_params


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--checkpoint_path", help="Folder(name) where the checkpoints and parameter config are saved.", type=str, required=True)
	
	args = parser.parse_args()
	checkpoint_path = args.checkpoint_path
	args = load_args(checkpoint_path)
	args.checkpoint_path = checkpoint_path

	model_params, optimizer_params = args_to_params(args)
	trainModule = TrainGraphColoring(model_params=model_params,
									 optimizer_params=optimizer_params, 
									 batch_size=args.batch_size,
									 checkpoint_path=args.checkpoint_path, 
									 debug=False,
									 multi_gpu=False)
	trainModule.evaluate_model()