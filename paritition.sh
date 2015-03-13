#/bin/sh
for folder in $(ls -p | grep -v move.sh) 
do
	mkdir ~/fbcunn_imagenet/imagenet_raw_images/selected/train/$folder
	mkdir ~/fbcunn_imagenet/imagenet_raw_images/selected/val/$folder
	cd $folder
	train=$(ls -l | wc -l)
	val=0
	thres=3750
	if [ $train -le $thres ]; then
		train=$(echo "$train * 0.8" | bc -l) 
		train=${train%.*}
		for file in $(ls -p | grep -v / | tail -$train) 
		do
			mv $file ~/fbcunn_imagenet/imagenet_raw_images/selected/train/$folder	
		done
		mv * ~/fbcunn_imagenet/imagenet_raw_images/selected/val/$folder
	else
		train=3000
		val=750	
		for file in $(ls -p | grep -v / | tail -$train) 
		do
			mv $file ~/fbcunn_imagenet/imagenet_raw_images/selected/train/$folder	
		done
		for file in $(ls -p | grep -v / | tail -$val) 
		do
			mv $file ~/fbcunn_imagenet/imagenet_raw_images/selected/val/$folder	
		done
	fi
	cd ../
done
