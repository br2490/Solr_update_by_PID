import sys
import getpass
import requests
import time

fix_list = ["bc%3Abulletin-19421105-2",
            "bc%3Abulletin-19421123-1",
            "bc%3Abulletin-19430604-5",
            "bc%3Abulletin-19431018-3",
            "bc%3Abulletin-19431111-4",
            "bc%3Abulletin-19440327-3",
            "bc%3Abulletin-19441102-4",
            "bc%3Abulletin-19450510-3",
            "bc%3Abulletin-19461118-4",
            "bc%3Abulletin-19470224-4",
            "bc%3Abulletin-19470304-2",
            "bc%3Abulletin-19471120-4",
            "bc%3Abulletin-19480927-4",
            "bc%3Abulletin-19481011-1",
            "bc%3Abulletin-19570506-3",
            "bc%3Abulletin-19571121-4",
            "bc%3Abulletin-19580109-3",
            "bc%3Abulletin-19580428-1",
            "bc%3Abulletin-19580505-1",
            "bc%3Abulletin-19581118-1",
            "bc%3Abulletin-19590309-3",
            "bc%3Abulletin-19591022-3",
            "bc%3Abulletin-19591026-1",
            "bc%3Abulletin-19600111-3",
            "bc%3Abulletin-19600208-3",
            "bc%3Abulletin-19600314-3",
            "bc%3Abulletin-19600321-3",
            "bc%3Abulletin-19601107-1",
            "bc%3Abulletin-19601117-1",
            "bc%3Abulletin-19610424-6",
            "bc%3Abulletin-19620215-1",
            "bc%3Abulletin-19620416-7",
            "bc%3Abulletin-19620419-4",
            "bc%3Abulletin-19620515-1",
            "bc%3Abulletin-19621001-3",
            "bc%3Abulletin-19621008-3",
            "bc%3Abulletin-19630114-1",
            "bc%3Abulletin-19630214-7",
            "bc%3Abulletin-19630225-2",
            "bc%3Abulletin-19630311-4",
            "bc%3Abulletin-19631031-1",
            "bc%3Abulletin-19661013-5",
            "bc%3Abulletin-19670209-7",
            "bc%3Abulletin-19670308-6",
            "bc%3Abulletin-19670308-8",
            "bc%3Abulletin-19670322-5",
            "bc%3Abulletin-19670427-7",
            "bc%3Abulletin-19671101-1",
            "bc%3Abulletin-19680508-1",
            "bc%3Abulletin-19681002-7",
            "bc%3Abulletin-19681023-3",
            "bc%3Abulletin-19681204-3",
            "bc%3Abulletin-19681211-4",
            "bc%3Abulletin-19690423-3",
            "bc%3Abulletin-19700218-2",
            "bc%3Abulletin-19710310-6",
            "bc%3Abulletin-19710428-8",
            "bc%3Abulletin-19710505-3",
            "bc%3Abulletin-19710923-8",
            "bc%3Abulletin-19711014-6",
            "bc%3Abulletin-19711118-4",
            "bc%3Abulletin-19720511-8",
            "bc%3Abulletin-19720907-2",
            "bc%3Abulletin-19730215-8",
            "bc%3Abulletin-19730301-5",
            "bc%3Abulletin-19730412-3",
            "bc%3Abulletin-19830309-3",
            "bc%3Abulletin-19830427-10",
            "bc%3Abulletin-19850917-4",
            "bc%3Abulletin-19850925-6",
            "bc%3Abulletin-19851002-8",
            "bc%3Abulletin-19861008-11",
            "bc%3Abulletin-19861029-5",
            "bc%3Abulletin-19861119-11",
            "bc%3Abulletin-19870304-6",
            "bc%3Abulletin-19870401-1",
            "bc%3Abulletin-19870401-10",
            "bc%3Abulletin-19871109-1",
            "bc%3Abulletin-19900402-5"]


def get_job():
    tomcat = input("Tomcat Server address and port [islandora:8080]: ")
    user = input("Fedora Administrator User [fedoraAdmin]: ")
    password = getpass.getpass(prompt='Fedora Admin Password [password will not be visible]: ', stream=None)
    tomcat = tomcat if tomcat else "islandora:8080"
    user = user if user else "fedoraAdmin"
    msg = ''.join(['Attempting to connect to ', tomcat, ' with username: ', user])
    print(msg)
    run_update(tomcat, user, password)


def run_update(tomcat, fgs_user, password):
    # FGS variables.
    rest_point = '/fedoragsearch/rest'
    fgs_pid_update_rest = '?operation=updateIndex&action=fromPid&value='
    fgs_url = ''.join(['http://', fgs_user, ':', password, '@', tomcat, rest_point])

    # Configure our session.
    webworker = requests.session()

    # Test login information.
    response = webworker.get(fgs_url)
    if response.status_code != 200:
        print('Error: Received a non-200 response during login.')
        sys.exit(1)
    print("Authenticated to FGS.")

    # Do all the things.
    for pid in fix_list:
        update_pid_url = ''.join([fgs_url, fgs_pid_update_rest, pid])
        this_pid = webworker.get(update_pid_url)
        print("{0} has been updated successfully.".format(pid)) if this_pid.status_code == 200 else \
            print("[WARN] {0} has NOT been updated.".format(pid))
        # Provide a delay so that we're not being jerk faces.
        time.sleep(1)


if __name__ == "__main__":
    get_job()
else:
    sys.exit(1)
