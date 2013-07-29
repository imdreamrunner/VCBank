import core

urls = (
    '/',                    'visitor.welcome.index',
    '/earn',                'visitor.welcome.earn',
    '/donate',              'visitor.welcome.donate',
    '/signup',              'visitor.account.create',
    '/login',               'visitor.account.login',
    '/account',             'visitor.account.display',
    '/logout',              'visitor.account.logout',
    '/admin',               'admin.manage.index',
    '/admin/dashboard',     'admin.manage.dashboard',
    '/admin/accounts',      'admin.manage.accounts',
    '/admin/accountsSearch','admin.manage.accountsSearch',
    '/admin/accountsLists', 'admin.manage.accountsLists',
    '/admin/accountsCreate','admin.manage.accountsCreate',
    '/admin/getAccounts',   'admin.manage.getAccounts',
    '/admin/login',         'admin.auth.login',
    '/admin/captcha.png',   'admin.auth.captcha'
)


if __name__ == "__main__":
    core.run(urls)