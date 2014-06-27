$(function() {
    // onload, update # of total posts
    var startingPosts = $('li[id^="post-"').length; 
    updatePostNumbers(startingPosts, startingPosts);

    // Handle adding tags to filter 
    $('#tag-filters button').click(function() {
        // Highlight the tag cloud and any other posts
        $(this).toggleClass("active").hide("fast");
        $('button[data-id="post-tag-' + $(this).attr("data-id") + '"]').removeClass("btn-default").addClass("btn-primary");
        filterPosts();
    });

    // Handle removal of tags 
    $(document).on(
        'click', 
        '#filtering-header button.remove-tag-container', 
        function() {
            var tagSlug = $(this).attr('data-id');
            var filterElement = $('#tag-filters button[data-id="' + tagSlug + '"]');
            filterElement.toggleClass("active").show("fast");
            $('button[data-id="post-tag-' + tagSlug + '"]').removeClass("btn-primary").addClass("btn-default");
            $(this).hide("fast");
            filterPosts();
        }
    );

    // Handle removal of all 
    $(document).on('click', '#clear-all-filters', resetFilters);
});

function filterPosts() {
    // filter posts once we update active filters
    // get active tag slugs & names 
    var activeTagSlugs = []
    var activeTagNames = []
    $('#tag-filters button.active').each(function(){
        activeTagSlugs.push($(this).attr("data-id"));
        activeTagNames.push($(this).text());
    });

    // Show & hide the posts that match the tag sets
    var posts = $('li[id^="post-"'); 
    var totalPosts = posts.length
    var postsShowing = 0
    posts.each(function() {
        // Create list of the post's tags
        var postTags = $(this).attr("data-id").split(/[ ]+/);
        // show the post if all of it's tags match the activeTagSlugs
        if (compareLists(activeTagSlugs, postTags)) {
            $(this).show("fast")
            postsShowing = postsShowing + 1;
        } else {
            $(this).hide("fast")
        }
    });
    // Update HTML to show we are filtering based on tags
    if (activeTagSlugs.length > 0) {
        var filterTags = "<h2>Tags:</h2> ";
        for (var i = 0; i < activeTagSlugs.length; i++) {
            filterTags += "<button class='btn btn-md btn-default tag-bubble remove-tag-container' data-id='" + activeTagSlugs[i] + "'>" + activeTagNames[i] + "<a href='#' class='remove-filter'>x</a></button>"
        };
        filterTags += "<a href='' id='clear-all-filters'>Clear All</a>"
        $('#filtering-header').html(filterTags);    
    } else {
        $('#filtering-header').html("<h2>All Posts</h2>");    
    }

    // finally update post numbers 
    updatePostNumbers(postsShowing, totalPosts);
}

function updatePostNumbers(postsShowing, totalPosts) {
    $('#posts-showing').html(postsShowing);
    $('#total-posts').html(totalPosts);
}

function compareLists(activeTagSlugs, postTags) {
    // Return true if all active tags are also in postTags, otherwise return false
    truthFlag = true;
    for (var i=0; i < activeTagSlugs.length; i++) {
        if (postTags.indexOf(activeTagSlugs[i]) === -1){
            truthFlag = false;
            break;
        }
    }
    return truthFlag;
}

function resetFilters() {
    // Show all posts & reset highlights
    var posts = $('li[id^="post-"'); 
    posts.each(function(){
        var buttons = $(this).children('button');
        buttons.removeClass("btn-primary").addClass("btn-default");
        $(this).show();
    });
    // Show all filters
    $('#tag-filters').children('button').each(function(){
        $(this).removeClass("active");
        $(this).show();
    });
    // Hide all tags
    $('#filtering-header').children('button').hide();
}

