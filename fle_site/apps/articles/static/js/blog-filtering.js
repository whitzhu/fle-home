$(function() {
    // onload, update # of total posts
    var startingPosts = $('li[id^="post-"').length; 
    updatePostNumbers(startingPosts, startingPosts);

    // Filter by tag
    $('#tag-filters button').click(function() {
        // Highlight the tag cloud and any other posts
        $(this).toggleClass("active");
        animateExplicitly($(this), "hide");
        $('button[data-id="post-tag-' + $(this).attr("data-id") + '"]').removeClass("btn-default").addClass("btn-primary");
        filterPosts();
    });

    // Remove filters 
    $(document).on(
        'click', 
        '#filtering-header button.remove-tag-container', 
        function() {
            var tagSlug = $(this).attr('data-id');
            var filterElement = $('#tag-filters button[data-id="' + tagSlug + '"]');
            filterElement.toggleClass("active")
            animateExplicitly(filterElement, "show");
            $('button[data-id="post-tag-' + tagSlug + '"]').removeClass("btn-primary").addClass("btn-default");
            animateExplicitly($(this), "hide");
            filterPosts();
        }
    );

    // Clear all  
    $(document).on('click', '#clear-all-filters', resetFilters); 
});

function filterPosts() {
    // filter posts once we update active filters
    
    var activeFilters = getFiltersByStatus(true);
    var activeFilterSlugs = getFilterProperties(activeFilters, "slug");
    var activeFilterNames = getFilterProperties(activeFilters, "name");

    // Show & hide the posts that match the tag sets
    var posts = $('li[id^="post-"]'); 
    var totalPosts = posts.length
    var postsShowing = 0

    posts.each(function() {
        // Create list of the post's tags
        var postTags = $(this).attr("data-id").split(/[ ]+/);
        // show the post if all of it's tags match the activeFilter tag slugs
        if (compareLists(activeFilterSlugs, postTags)) {
            animateExplicitly($(this), "show");
            postsShowing = postsShowing + 1;
        } else {
            animateExplicitly($(this), "hide");
        }
    });

    // Update HTML to show we are filtering based on tags
    if (activeFilterSlugs.length > 0) {
        var filterTags = "<h2>Tags:</h2> ";
        for (var i = 0; i < activeFilterSlugs.length; i++) {
            filterTags += "<button class='btn btn-md btn-default tag-bubble remove-tag-container' data-id='" + activeFilterSlugs[i] + "'>" + activeFilterNames[i] + "<a href='#' class='remove-filter'>x</a></button>"
        };
        filterTags += "<a href='' id='clear-all-filters'>Clear All</a>"
        $('#filtering-header').html(filterTags);    
    } else {
        $('#filtering-header').html("<h2>All Posts</h2>");    
    }

    // update post numbers & disable unusable filters
    updatePostNumbers(postsShowing, totalPosts);
    smartFilterDisabling()
}

function getFiltersByStatus(active){
    // Return a list of active or inactive filter slugs, and a list of filter names
    // get active tag slugs & names 
    var tagObjects = []
    if (active){
        var tagFilter = $('#tag-filters button.active');
    } else {
        var tagFilter = $('#tag-filters button:not(.active)')
    }
    tagFilter.each(function(){
        tagObjects.push($(this));
    });
    return tagObjects;
}

function getFilterProperties(filters, property) {
    // Return list of all filter properties (either names or slugs)
    var filterProps = [];
    if (property === "slug") {
        var filterProps = $.map(filters, function(element) { return element.attr("data-id")});
    } else if (property === "name") {
        var filterProps = $.map(filters, function(element) { return element.text()});
    }
    return filterProps;
}

function updatePostNumbers(postsShowing, totalPosts) {
    $('#posts-showing').html(postsShowing);
    $('#total-posts').html(totalPosts);
}

function smartFilterDisabling(){
    // Disable filters that would lead to 0 posts displaying
    // when combined with currently active filters
    var inactiveFilters = getFiltersByStatus(false);

    // For each one, check if it is a tag of any current post
    var posts = $('#post-list li[id^="post-"').filter(function(){
        var element = $(this);
        if (element.attr("data-visible") === "false") {
            return false;
        }
        return true;
    });

    var allPostTags = [] 
    posts.each(function(){
        var postTags = $(this).attr("data-id").split(/[ ]+/);
        allPostTags = arrayUnique(allPostTags.concat(postTags));
    });


    for (var i = 0; i < inactiveFilters.length; i++) {
        if (allPostTags.indexOf(inactiveFilters[i].attr("data-id")) >= 0) {
            inactiveFilters[i].prop("disabled", false);
        } else {
            inactiveFilters[i].prop("disabled", true);
        }
    };
}

function resetFilters() {
    // Show all posts & reset highlights
    var posts = $('li[id^="post-"'); 
    posts.each(function(){
        var buttons = $(this).children('button');
        buttons.removeClass("btn-primary").addClass("btn-default");
        animateExplicitly($(this), "show");
    });
    // Show all filters
    $('#tag-filters').children('button').each(function(){
        $(this).removeClass("active");
        animateExplicitly($(this), "show");
    });
    // Hide all tags
    animateExplicitly($('#filtering-header').children('button'), "hide");
}

function compareLists(tagSlugs, postTags) {
    // Return true if all tags are also in postTags, otherwise return false
    truthFlag = true;
    for (var i=0; i < tagSlugs.length; i++) {
        if (postTags.indexOf(tagSlugs[i]) === -1){
            truthFlag = false;
            break;
        }
    }
    return truthFlag;
}

// thx http://stackoverflow.com/a/1584377
function arrayUnique(array) {
    var a = array.concat();
    for(var i=0; i<a.length; ++i) {
        for(var j=i+1; j<a.length; ++j) {
            if(a[i] === a[j])
                a.splice(j--, 1);
        }
    }

    return a;
}

function animateExplicitly(element, animation){
    // Call jQuery show/hide method after adding an attribute to 
    // indicate visibility (so we can check for it later in the code)
    if (animation === "show"){
        element.attr("data-visible", true);
        element.show("fast")
    } else if (animation === "hide") {
        element.attr("data-visible", false);
        element.hide("fast")
    }
}
