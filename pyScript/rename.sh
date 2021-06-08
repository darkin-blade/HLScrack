for ts in /media/lynx/D/Download_D/AndroidShare/ImageShare/潭州1/*
do
  input_name=${ts}
  if [[ ${input_name} =~ "_ts" ]]
  then
    # 以_ts结尾
    output_name=${input_name%_ts}.ts
    # echo ${output_name}
    mv ${input_name} ${output_name}
  fi
done
