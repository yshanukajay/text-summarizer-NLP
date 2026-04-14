from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, trainer
from transformers import Trainer, TrainingArguments
from transformers import DataCollatorForSeq2Seq
from datasets import load_from_disk
import torch
from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.entity import ModelTrainerConfig
import os

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)

        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)

        train_dataset = load_from_disk(self.config.data_path)["train"]

        training_args = TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=self.config.num_train_epochs,
            warmup_steps=self.config.warmup_steps,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            weight_decay=self.config.weight_decay,
            logging_steps=self.config.logging_steps,
            evaluation_strategy=self.config.evaluation_strategy,
            eval_steps=self.config.eval_steps,
            save_steps=self.config.save_steps,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps
        )

        trainer_args = TrainingArguments(
            output_dir='pegasus-samsum', num_train_epochs=1, warmup_steps=500,
            per_device_train_batch_size=1, per_device_eval_batch_size=1,
            weight_decay=0.01, logging_steps=10,
            eval_strategy='steps', eval_steps=500, save_steps=1e6,
            gradient_accumulation_steps=16
        )

        trainer.train()

        model_pegasus.save_pretrained(os.path.join(self.config.root_dir, "model"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))
