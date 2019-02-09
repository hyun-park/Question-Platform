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

        $.each($(".question-card"), function (index, question) {
            if(isEmpty) {
                $(question).removeClass("d-none");
            } else {
                if(isSearchedQuestions[index]) {
                    $(question).removeClass("d-none");
                } else {
                    $(question).addClass("d-none");
                }
            }
        });
    }
})();