##################################################################################
#####    Shell script to extract valid dataset files from the total dataset   #########
##################################################################################

filename1="/home/aisha/test_mt_law/training_data/en-ar-law-source.bpe"  # Specify the path to source dataset file
filename2="/home/aisha/test_mt_law/training_data/en-ar-law-target.bpe"  # Specify the path to target dataset file
filename3="/home/aisha/test_mt_law/training_data/enarlawtest.talp"     # Specify the path to alignment file (.talp)

line_count="$(wc -l < "$filename1")"
valid_size=100                      ## Specify the validation dataset size
segments=$( expr "$valid_size" '/' 100 )
batch=$( expr "$line_count" '/' "$segments" )
echo "batch size: $batch "
echo "Number of segments: $segments"

for (( i="$segments"; i>=1; i-- ))
do
echo "welcome $i times"
min=$( expr "$batch" '*' '(' "$i" '-' 1 ')' )
max=$( expr "$batch" '*' "$i" )
echo "min: $min "
echo "max: $max "
line_nums_to_delete="$(shuf -i "$min-$max" -n 100)"
sed_script1="$(printf '%dp;' $line_nums_to_delete)"
sed_script2="$(printf '%dd;' $line_nums_to_delete)"

## Specify the path to the output valid source file
sed -n "$sed_script1" "$filename1" >> /home/aisha/test_mt_law/training_data/output_En-Ar-Law.src.bpe.valid
sed -i -e "$sed_script2" "$filename1"

## Specify the path to the output valid target file
sed -n "$sed_script1" "$filename2" >> /home/aisha/test_mt_law/training_data/output_En-Ar-Law.tgt.bpe.valid
sed -i -e "$sed_script2" "$filename2"

## Specify the path to the output valid alignment files
sed -n "$sed_script1" "$filename3" >> /home/aisha/test_mt_law/training_data/output_En-Ar-Law.talp.valid
sed -i -e "$sed_script2" "$filename3"
done
