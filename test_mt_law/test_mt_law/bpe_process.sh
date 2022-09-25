##################################################################################################################
#####   Shell script to train a BPE model on the dataset, then converting the dataset into BPE subwords   ########
##################################################################################################################


## 1- Specify the paths to the input data files both source and target
## Do not change outputfile.joint
cat /home/aisha/test_mt_law/input-bpe/source_tok /home/aisha/test_mt_law/input-bpe/target_tok > outputfile.joint

spm_train --input_sentence_size      100000000 \
          --model_prefix             /home/aisha/test_mt_law/bpe-output/bpe_en-ar-law_model \
          --model_type               bpe \
          --num_threads              4 \
          --split_by_unicode_script  1 \
          --split_by_whitespace      1 \
          --remove_extra_whitespaces 1 \
          --add_dummy_prefix         0 \
          --normalization_rule_name  identity \
          --vocab_size               400 \
          --character_coverage       1.0 \
          --add_dummy_prefix         1 \
          --input                    outputfile.joint


## 4- Specify the paths to the output BPE model and input data files and output BPE encoded data files
spm_encode --model /home/aisha/test_mt_law/bpe-output/bpe_en-ar-law_model.model < /home/aisha/test_mt_law/input-bpe/source_tok > /home/aisha/test_mt_law/bpe-output/en-ar-law-source.bpe
spm_encode --model /home/aisha/test_mt_law/bpe-output/bpe_en-ar-law_model.model < /home/aisha/test_mt_law/input-bpe/target_tok > /home/aisha/test_mt_law/bpe-output/en-ar-law-target.bpe
