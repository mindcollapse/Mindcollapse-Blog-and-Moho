$(function(){
	$('.blogs-post.change-form #id_text').redactor({ 
		minHeight: 700,
		wym: true,
		fixedBox: true,
		fixed: true,
		imageUpload: '/godmode/blog_upload_file',
		fileUpload: '/godmode/blog_upload_file'
	}); 

	/* dont need any WYSIWYG in MOHO, disable it 
	$('.mohos-moho.change-form #id_text').redactor({ 
		minHeight: 300,
		wym: true,
		fixedBox: true,
		fixed: true
	}); 

	*/

});
