/*
 * JavaScript file for the application to demonstrate
 * using the API
 */

// Create the namespace instance
let ns = {};

// Create the model instance
ns.model = (function() {
    'use strict';

    let $event_pump = $('body');

    // Return the API
    return {
        'read': function() {
            let ajax_options = {
                type: 'GET',
                url: 'api/people',
                accepts: 'application/json',
                dataType: 'json'
            };
            $.ajax(ajax_options)
                .done(function(data) {
                    $event_pump.trigger('model_read_success', [data]);
                })
                .fail(function(xhr, textStatus, errorThrown) {
                    $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
                })
        },
        create: function(first_name, last_name) {
            let ajax_options = {
                type: 'POST',
                url: 'api/people',
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify({
                    'first_name': first_name,
                    'last_name': last_name
                })
            };
            $.ajax(ajax_options)
                .done(function(data) {
                    $event_pump.trigger('model_create_success', [data]);
                })
                .fail(function(xhr, textStatus, errorThrown) {
                    $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
                })
        },
        update: function(first_name, last_name, name) {
            let ajax_options = {
                type: 'PUT',
                url: 'api/people/' + name,
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify({
                    'first_name': first_name,
                    'last_name': last_name
                })
            };
            $.ajax(ajax_options)
                .done(function(data) {
                    $event_pump.trigger('model_update_success', [data]);
                })
                .fail(function(xhr, textStatus, errorThrown) {
                    $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
                })
        },
        'delete': function(name) {
            let ajax_options = {
                type: 'DELETE',
                url: 'api/people/' + name,
                accepts: 'application/json',
                contentType: 'plain/text'
            };
            $.ajax(ajax_options)
                .done(function(data) {
                    $event_pump.trigger('model_delete_success', [data]);
                })
                .fail(function(xhr, textStatus, errorThrown) {
                    $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
                })
        }
    };
}());

// Create the view instance
ns.view = (function() {
    'use strict';

    let $first_name = $('#first_name'),
        $last_name = $('#last_name'),
        $name = $('#name');

    // return the API
    return {
        reset: function() {
            $last_name.val('');
            $first_name.val('').focus();
        },
        update_editor: function(first_name, last_name) {
            $last_name.val(last_name);
            $first_name.val(first_name).focus();
        },
        build_table: function(people) {
            let rows = ''

            // clear the table
            $('.people table > tbody').empty();

            // did we get a people array?
            if (people) {
                for (let i = 0, l = people.length; i < l; i++) {
                    rows += `<tr><td class="first_name">${people[i].first_name}</td><td class="last_name">${people[i].last_name}</td><td>${people[i].birth_date}</td></tr>`;
                }
                $('table > tbody').append(rows);
            }
        },
        error: function(error_msg) {
            $('.error')
                .text(error_msg)
                .css('visibility', 'visible');
            setTimeout(function() {
                $('.error').css('visibility', 'hidden');
            }, 3000)
        }
    };
}());

// Create the controller
ns.controller = (function(m, v) {
    'use strict';

    let model = m,
        view = v,
        $event_pump = $('body'),
        $first_name = $('#first_name'),
        $last_name = $('#last_name'),
        $birth_date = $('#birth_date'),
        $name = $('#name');

    // Get the data from the model after the controller is done initializing
    setTimeout(function() {
        model.read();
    }, 100)

    // Validate input
    function validate(first_name, last_name) {
        return first_name !== "" && last_name !== "";
    }

    // Create our event handlers
    $('#create').click(function(e) {
        let first_name = $first_name.val(),
            last_name = $last_name.val(),
            name = $name.val();

        e.preventDefault();

        if (validate(first_name, last_name)) {
            model.create(first_name, last_name)
        } else {
            alert('Problem with first or last name input');
        }
    });

    $('#update').click(function(e) {
        let first_name = $first_name.val(),
            last_name = $last_name.val();

        e.preventDefault();

        if (validate(first_name, last_name)) {
            model.update(first_name, last_name)
        } else {
            alert('Problem with first or last name input');
        }
        e.preventDefault();
    });

    $('#delete').click(function(e) {
        let last_name = $last_name.val();

        e.preventDefault();

        if (validate('placeholder', last_name)) {
            model.delete(last_name)
        } else {
            alert('Problem with first or last name input');
        }
        e.preventDefault();
    });

    $('#reset').click(function() {
        view.reset();
    })

    $('table > tbody').on('dblclick', 'tr', function(e) {
        let $target = $(e.target),
            first_name,
            last_name;

        first_name = $target
            .parent()
            .find('td.first_name')
            .text();

        last_name = $target
            .parent()
            .find('td.last_name')
            .text();

        view.update_editor(first_name, last_name);
    });

    // Handle the model events
    $event_pump.on('model_read_success', function(e, data) {
        view.build_table(data);
        view.reset();
    });

    $event_pump.on('model_create_success', function(e, data) {
        model.read();
    });

    $event_pump.on('model_update_success', function(e, data) {
        model.read();
    });

    $event_pump.on('model_delete_success', function(e, data) {
        model.read();
    });

    $event_pump.on('model_error', function(e, xhr, textStatus, errorThrown) {
        let error_msg = textStatus + ': ' + errorThrown + ' - ' + xhr.responseJSON.detail;
        view.error(error_msg);
        console.log(error_msg);
    })
}(ns.model, ns.view));