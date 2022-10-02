##################################################################################
#####    Shell script to extract valid dataset files from the total dataset   #########
##################################################################################

filename1=$1  # Specify the path to source dataset file
filename2=$2  # Specify the path to target dataset file
filename3=$3     # Specify the path to alignment file (.talp)

line_count="$(wc -l < "$filename1")"
valid_size=$4                     ## Specify the validation dataset size
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
line_nums_to_delete="$(shuf -i "$min-$max" -n ${valid_size})"
sed_script1="$(printf '%dp;' $line_nums_to_delete)"
sed_script2="$(printf '%dd;' $line_nums_to_delete)"

## Specify the path to the output valid source file
sed -n "$sed_script1" "$filename1" >> ${filename1}.valid
sed -i -e "$sed_script2" "$filename1"

## Specify the path to the output valid target file
sed -n "$sed_script1" "$filename2" >> ${filename2}.valid
sed -i -e "$sed_script2" "$filename2"

## Specify the path to the output valid alignment files
sed -n "$sed_script1" "$filename3" >> ${filename3}.valid
sed -i -e "$sed_script2" "$filename3"
done
mkdir /root/training_data_consumer
mv $filename1 /root/training_data_consumer/train.en
mv $filename2 /root/training_data_consumer/train.arb
mv $filename1 /root/training_data_consumer/train.align
mv ${filename1}.valid /root/training_data_consumer/valid.en
mv ${filename2}.valid /root/training_data_consumer/valid.arb
mv ${filename1}.valid /root/training_data_consumer/valid.align
