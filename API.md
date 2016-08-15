# API Design for iis_shim

## iis.site
- get_all `DONE`
- get_by_id `DONE`
- get_by_name `DONE`
- get_by_state `DONE`
- get_by_bindings `DONE`
- stop_by_id `DONE`
- start_by_id `DONE`
- length `DONE`

## iis.app
- get_all `DONE`
- get_by_name `DONE`
- get_by_site_name `DONE`
- get_by_poolname `DONE`
- get_by_sitename `DONE`
- length `DONE`

## iis.pool
- get_all `DONE`
- get_by_name `DONE`
- get_by_pipelinemode `DONE`
- get_by_runtimeversion `DONE`
- get_by_state `DONE`
- get_by_site_id `DONE`
- stop_by_site_id `DONE`
- start_by_site_id `DONE`
- length `DONE`

## iis.vdir
- get_all `DONE`
- get_by_name `DONE`
- get_by_physicalpath `DONE`
- get_by_path `DONE`
- get_by_appname `DONE`
- get_by_site_id `DONE`
- length `DONE`

## iis.wp
- get_by_name `DONE`
- get_by_poolname `DONE`
- length `DONE`

## iis.request
- get_by_name
- get_by_siteid
- get_by_verb
- get_by_clientip
- get_by_wpname
- get_by_poolname


## Relationship between iis components

    app
        app.name        <1>
        apppool.name    <2>
        site.name       <3>`
    pool
        apppool.name    <2>
        runtimeversion
        state
        pipelinemode
    site
        site.name       <3>`
        id
        binding
        state
    vdir
        physicalpath
        path
        app.name        <1>
        vdir.name

    site.id > site.name > app.name > apppool.name > *control_apppool*
    site.id > site.name > app.name > physicalpath > *change_path*
