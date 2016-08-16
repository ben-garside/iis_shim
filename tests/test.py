import iis_shim as iis
import unittest

def fun(x):
    return x + 1

class iis_site_tests(unittest.TestCase):
    def test_get_all_1(self):
        """
        Check if the number of sites returned match the number
        of apps
        """
        apps = iis.app.get_all()
        sites = iis.site.get_all()
        self.assertEqual(len(apps),len(sites))
    def test_get_by_id(self):
        """
        Check that you can retrieve a site using its ID
        """
        sites_id = (iis.site.get_all()[0]).get('SITE.ID')
        sites_name = (iis.site.get_all()[0]).get('SITE.NAME') 
        name = (iis.site.get_by_id(1)).get('SITE.NAME') 
        self.assertEqual(sites_name, name)
    def test_get_by_id_wrongtype(self):
        self.assertRaises(TypeError, iis.site.get_by_id,"1")
    
    def test_get_by_name_not_partial(self):
        """
        Check get_by_name returns the site with the given Name
        -- Partial not set
        """
        sites_name = (iis.site.get_all()[0]).get('SITE.NAME')
        get_name = (iis.site.get_by_name(sites_name)).get('SITE.NAME')
        self.assertEqual(sites_name, get_name)
    def test_get_by_name_not_partial_wrongtype(self):
        self.assertRaises(TypeError, iis.site.get_by_name, 121)

    def test_get_by_name_partial(self):
        """
        Checks whether you can search for a website using
        a substring of the name
        """
        sites_name = (iis.site.get_all()[0]).get('SITE.NAME')
        get_name = (iis.site.get_by_name(sites_name[:2], partial=True))
        for name in get_name:
            if name.get('SITE.NAME') == sites_name:
                self.assertTrue(True)
                return
        self.assertTrue(False)
    def test_get_by_state_start(self):
        self.assertRaises(TypeError, iis.site.get_by_state, [])
    def test_get_by_state_start(self):
        """
        Checks whether all sites in the start state are returned
        """
        all_sites = iis.site.get_all()
        counter_start = 0
        for site in all_sites:
            if site.get('state') == 'Started':
                counter_start += 1
        started_sites = iis.site.get_by_state("Started")
        self.assertEqual(counter_start, len (started_sites))
    
    def test_get_by_state_stopped(self):
        """
        Checks whether all sites in the stop state are returned
        """
        all_sites = iis.site.get_all()
        counter_end = 0
        for site in all_sites:
            if site.get('state') == 'Stopped':
                counter_end += 1
        stopped_sites = iis.site.get_by_state("Stopped")
        self.assertEqual(counter_end, len(stopped_sites))
    def test_get_by_bindings_not_partial(self):
        """
        Checks whether you can search for a site based on its full binding
        """
        sites_binding = (iis.site.get_all()[0]).get('bindings')
        get_binding = (iis.site.get_by_bindings(sites_binding)).get('bindings')
        self.assertEqual(sites_binding, get_binding)
    def test_get_by_bindings_partial(self):
        """
        Checks whether you can search for a site using partial bindings
        """
        sites_binding = (iis.site.get_all()[0]).get('bindings')
        get_bindings = (iis.site.get_by_bindings(sites_binding[2:],partial=True))
        for binding in get_bindings:
            if (binding.get('bindings') == sites_binding):
                self.assertTrue(True)
                return
        self.assertTrue(False)
    def test_get_by_bindings_wrongtype(self):
        self.assertRaises(TypeError, iis.site.get_by_bindings, {})
    def test_stop_by_id(self): 
        """
        Retreives the first started website if any and then stops it.
        """
        sites = iis.site.get_all()
        site_id = (-1)
        for site in sites:
            state = site.get('state')
            if (state == "Started"):
                site_id = int(site.get('SITE.ID'))
                break
        if (site_id > -1):
            iis.site.stop_by_id(site_id)
            site_state = (iis.site.get_all()[0]).get('state')
            self.assertEqual("Stopped", site_state)
            return
        self.assertTrue(False, "All sites are stopped, please start a site")
    def test_start_by_id(self):
        sites = iis.site.get_all()
        site_id = (-1)
        for site in sites:
            state = site.get('state')
            if (state == "Stopped"):
                site_id = int(site.get('SITE.ID'))
                break
        if (site_id > -1):
            iis.site.start_by_id(site_id)
            site_state = (iis.site.get_all()[0]).get('state')
            self.assertEqual("Started", site_state)
            return
        assertTrue(False, "All sites are started, please stop a site")
    def test_length(self):
        self.assertEqual(len(iis.site.get_all()),iis.site.length())
    def test_start_by_id_wrongtype(self):
        self.assertRaises(TypeError, iis.site.start_by_id, [])


class iis_app_tests(unittest.TestCase):
    def test_get_all(self):
        """
        Check if the number of sites returned match the number
        of apps
        """
        apps = iis.app.get_all()
        sites = iis.site.get_all()
        self.assertEqual(len(apps),len(sites))
    def test_get_by_name_not_partial(self):
        """
        Check get_by_name returns the app with the given Name
        -- Partial not set
        """
        app_name = (iis.app.get_all()[0]).get('APP.NAME')
        get_name = (iis.app.get_by_name(app_name)).get('APP.NAME')
        self.assertEqual(app_name, get_name)
    def test_get_by_name_partial(self):
        """
        Checks whether you can search for a app using
        a substring of the name
        """
        app_names = (iis.app.get_all()[0]).get('APP.NAME')
        get_name = (iis.app.get_by_name(app_names[:2], partial=True))
        for name in get_name:
            if name.get('APP.NAME') == app_names:
                self.assertTrue(True)
                return
        self.assertTrue(False)
    def test_get_by_name_wrongtype(self):
        self.assertRaises(TypeError, iis.app.get_by_name, 121)
    def test_get_by_site_name_no_partial(self):
        """
        Checks wheter you can get an app by using its site name
        -- Partial not set
        """
        site_name = (iis.app.get_all()[0]).get('SITE.NAME')
        get_name = (iis.app.get_by_site_name(site_name)).get('SITE.NAME')
        self.assertEqual(site_name, get_name)
    def test_get_by_site_name_partial(self):
        site_name = (iis.app.get_all()[0]).get('SITE.NAME')
        get_name = (iis.app.get_by_name(site_name[:2], partial=True))
        for name in get_name:
            if name.get('SITE.NAME') == site_name:
                self.assertTrue(True)
                return
        self.assertTrue(False)
    def test_get_by_site_name_wrong_type(self):
        self.assertRaises(TypeError, iis.app.get_by_site_name, 121)
    def test_get_by_pool_not_partial(self):
        pool_name = (iis.app.get_all()[0]).get('APPPOOL.NAME')
        get_pool_name = (iis.app.get_by_pool_name(pool_name)).get('APPPOOL.NAME')
        self.assertEqual(pool_name, get_pool_name)
    def test_get_by_pool_partial(self):
        pool_name = (iis.app.get_all()[0]).get('APPPOOL.NAME')
        get_pool_name = (iis.app.get_by_pool_name(pool_name[:2], partial=True))
        for name in get_pool_name:
            if name.get('APPPOOL.NAME') == pool_name:
                self.assertTrue(True)
                return
        self.assertTrue(False)  
    def test_get_by_pool_name_wrong_type(self):
        self.assertRaises(TypeError, iis.app.get_by_pool_name, 122)
         
     
class iis_pool_tests(unittest.TestCase):
    def test_get_all(self):
        """
        Check if the number of sites returned match the number
        of apps
        """
        pools = iis.pool.get_all()
        app = iis.app.get_all()
        self.assertEqual(len(app),len(pools))
    def test_get_by_name_not_partial(self):
        """
        Check get_by_name returns the app with the given Name
        -- Partial not set
        """
        pool_name = (iis.pool.get_all()[0]).get('APPPOOL.NAME')
        get_name = (iis.pool.get_by_name(pool_name)).get('APPPOOL.NAME')
        self.assertEqual(pool_name, get_name)
    def test_get_by_name_partial(self):
        """
        Checks whether you can search for a app using
        a substring of the name
        """
        pool_name = (iis.pool.get_all()[0]).get('APPPOOL.NAME')
        get_name = (iis.pool.get_by_name(pool_name[:2], partial=True))
        for name in get_name:
            if name.get('APPPOOL.NAME') == pool_name:
                self.assertTrue(True)
                return
        self.assertTrue(False)
    def test_get_by_name_wrong_type(self):
        self.assertRaises(TypeError, iis.pool.get_by_name, 112)
    def test_get_by_pipelinemode(self):
        pipelinemode_name = (iis.pool.get_all()[0]).get('PipelineMode')
        get_by_plm = (iis.pool.get_by_PipelineMode(pipelinemode_name))
        for pool in get_by_plm:
            if pool.get('PipelineMode') == pipelinemode_name:
                self.assertTrue(True)
                return
        self.assertTrue(False)
    def test_get_by_pipelinemode_wrong_type(self):
        self.assertRaises(TypeError, iis.pool.get_by_PipelineMode, 112)
    def test_get_by_runtimeversion(self):
        test_runtime_version = (iis.pool.get_all()[0]).get('RuntimeVersion') 
        get_by_runtime = iis.pool.get_by_runtimeverion(test_runtime_version)
        for app in get_by_runtime:
            if app.get('RuntimeVersion') == test_runtime_version:
                continue
            self.assertTrue(False)
        self.assertTrue(True)
    def test_get_by_state_start(self):
        self.assertRaises(TypeError, iis.pool.get_by_state, [])
    def test_get_by_state_start(self):
        """
        Checks whether all pools in the start state are returned
        """
        pools = iis.pool.get_all()
        counter_start = 0
        for pool in pools:
            if pool.get('state') == 'Started':
                counter_start += 1
        started_pools = iis.pool.get_by_state("Started")
        self.assertEqual(counter_start, len (started_pools))
    
    def test_get_by_state_stopped(self):
        """
        Checks whether all pools in the stop state are returned
        """
        pools = iis.pool.get_all()
        counter_end = 0
        for pool in pools:
            if pool.get('state') == 'Stopped':
                counter_end += 1
        stopped_pools = iis.pool.get_by_state("Stopped")
        self.assertEqual(counter_end, len(stopped_pools))
    def test_get_by_site_id(self):
        """
        Retreives the site id of a site and then uses that to obtain the app pool
        """
        site_id = iis.site.get_all()[0].get('SITE.ID')
        app_pool = iis.pool.get_by_site_id(int(site_id))
        self.assertTrue(type(app_pool) is dict)
    def test_stop_by_site_id(self):
        """
        Retrieves a list of sites, looks for the first started one, extracts id
        and stops the corresponding app pool
        """
        sites = iis.site.get_all()
        site_id = (-1)
        for site in sites:
            state = site.get('state')
            if (state == "Started"):
                site_id = int(site.get('SITE.ID'))
                break
        if (site_id > -1):
            iis.pool.stop_by_site_id(site_id)
            pool_state = (iis.pool.get_by_site_id(site_id)).get('state')
            self.assertEqual("Stopped", pool_state)
            return
        self.assertTrue(False, "All sites are stopped, please start a site")
    def test_start_by_site_id(self):
        """
        Retrieves a list of sites. looks for the first stopped one, extracts and
        stops the corresponding app pool
        """        
        sites = iis.site.get_all()
        site_id = (-1)
        for site in sites:
            state = site.get('state')
            if (state == "Stopped"):
                site_id = int(site.get('SITE.ID'))
                break
        if (site_id > -1):
            iis.pool.start_by_site_id(site_id)
            pool_state = (iis.pool.get_by_site_id(site_id)).get('state')
            self.assertEqual("Started", pool_state)
            return
        self.assertTrue(False, "All sites are started please stop a site")
    def test_length(self):
        self.assertEqual(iis.pool.length(), len(iis.pool.get_all()))

class iis_vdi_tests(unittest.TestCase):
    def test_get_all(self):
        """
        Checks whether the number of vdirs returned matches the number of sites returned
        """
        vdirs = iis.vdir.get_all()
        sites = iis.site.get_all()
        self.assertEqual(len(vdirs), len(sites))
    def test_get_by_name_no_partial(self):
        """
        Checks whether the number of vdirs returned is the same as the nummber of sites
        """        
        vdir_name = (iis.vdir.get_all()[0]).get('APP.NAME')
        get_vdir_name = (iis.vdir.get_by_name(vdir_name)).get('APP.NAME')
        self.assertEqual(vdir_name, get_vdir_name)
    def test_get_by_name_partial(self):
        """
        Checks whether you can search for a vdir using
        a substring of the name
        """
        vdir_name = (iis.vdir.get_all()[0]).get('APP.NAME')
        get_name = (iis.vdir.get_by_name(vdir_name[:2], partial=True))
        for name in get_name:
            if name.get('APP.NAME') == vdir_name:
                self.assertTrue(True)
                return
        self.assertTrue(False)        
    def test_get_by_physicalpath_not_partial(self):
        vdir_physicalpath = (iis.vdir.get_all()[0]).get('physicalPath')
        get_physical_path = (iis.vdir.get_by_physicalpath(vdir_physicalpath)).get('physicalPath')
        self.assertEqual(vdir_physicalpath, get_physical_path)
    def test_get_by_phyiscal_path_partial(self):
        """
        Checks whether you can search for a vdir using
        a substring of the physical path
        """
        vdir_physicalpath = (iis.vdir.get_all()[0]).get('physicalPath')
        get_name = (iis.vdir.get_by_name(vdir_physicalpath[:2], partial=True))
        for name in get_name:
            if name.get('physicalPath') == vdir_physicalpath:
                self.assertTrue(True)
                return
        self.assertTrue(False)
    def test_get_by_path_not_partial(self):
        vdir_path = (iis.vdir.get_all()[0]).get('path')
        get_path = (iis.vdir.get_by_path(vdir_path)).get('path')
        self.assertEqual(vdir_path, get_path)
    def test_get_by_phyiscal_path_partial(self):
        """
        Checks whether you can search for a vdir using
        a substring of the path
        """
        vdir_path = (iis.vdir.get_all()[0]).get('path')
        get_name = (iis.vdir.get_by_path(vdir_path[:2], partial=True))
        for name in get_name:
            if name.get('path') == vdir_path:
                self.assertTrue(True)
                return
        self.assertTrue(False) 
    def test_get_by_app_name_not_partial(self):
        vdir_name = (iis.vdir.get_all()[0]).get('APP.NAME')
        get_vdir_name = (iis.vdir.get_by_app_name(vdir_name)).get('APP.NAME')
        self.assertEqual(vdir_name, get_vdir_name)
    def test_get_by_app_name_partial(self):
        vdir_name = (iis.vdir.get_all()[0]).get('APP.NAME')
        get_name = (iis.vdir.get_by_app_name(vdir_name[:2], partial=True))
        for name in get_name:
            if name.get('APP.NAME') == vdir_name:
                self.assertTrue(True)
                return
        self.assertTrue(False)
    def test_get_by_site_id(self):
        """
        Retreives the site id of a site and then uses that to obtain the vdir
        """
        site_id = iis.site.get_all()[0].get('SITE.ID')
        app_pool = iis.vdir.get_by_site_id(int(site_id))
        self.assertTrue(type(app_pool) is dict)
    def test_length(self):
        """
        Checks whether length correctly counts all the current vdirs
        """
        self.assertEqual(iis.vdir.length(), len(iis.vdir.get_all()))

           


    

           
        





    


        
if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(iis_site_tests)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(iis_app_tests)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(iis_pool_tests)
    suite4 = unittest.TestLoader().loadTestsFromTestCase(iis_vdi_tests)
    allTests = unittest.TestSuite([suite1, suite2, suite3 , suite4])
    unittest.TextTestRunner(verbosity=2).run(suite4)