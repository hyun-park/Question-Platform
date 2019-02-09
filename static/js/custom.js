(function () {
    $("#search-input").on("change paste keyup", function() {
        let query = $(this).val();
        if(query == "") {
            getQuestions(query, true)
        } else {
            getQuestions(query, false)
        }

    })

    function getQuestions(query, isEmpty) {
        let isSearchedQuestions = $.map($(".question-card").find(".card-title"), function(val, i){
          return val.innerText.replace(' (삭제)','').includes(query);
        });

        let isNotFound = isSearchedQuestions.every(function (isFound) {
            return !isFound
        });


        if(isEmpty) {
            $(".question-card").removeClass("d-none");
        } else {
            if(isNotFound) {
                $(".question-card").addClass("d-none");
                $("#question-not-found").removeClass("d-none");
            } else {
                $("#question-not-found").addClass("d-none");
                $.each($(".question-card"), function (index, question) {
                    if(isSearchedQuestions[index]) {
                        $(question).removeClass("d-none");
                    } else {
                        $(question).addClass("d-none");
                    }
                });
            }
        }
    }
})();