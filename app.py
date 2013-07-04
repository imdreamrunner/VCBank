import core

urls = (
    '/',            'visitor.welcome.index',
    '/earn',        'visitor.welcome.earn',
    '/donate',      'visitor.welcome.donate',
    '/signup',      'visitor.account.create',
    '/login',       'visitor.account.login',
    '/account',     'visitor.account.display',
    '/logout',      'visitor.account.logout',
)


if __name__ == "__main__":
    core.run(urls)